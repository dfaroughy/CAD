from __future__ import annotations

import json
import os
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .dataset import CADDrawingDataset, DrawingSample


DEFAULT_SYSTEM_PROMPT = (
    "You are an expert CAD reverse-engineering assistant. "
    "Given a technical drawing image, produce CadQuery Python code that reconstructs the part. "
    "Return only valid Python code, preferably as a stepwise sequence (step1, step2, ...) ending with `result`."
)

DEFAULT_USER_PROMPT = (
    "Analyze this engineering drawing and write CadQuery code that recreates the object. "
    "Use clear step-by-step construction variables (step1, step2, ...) and assign final geometry to `result`. "
    "Do not include explanations outside the code."
)


@dataclass(frozen=True)
class VLMInferenceConfig:
    model: str = "openai/gpt-4o"
    temperature: float = 0.0
    max_tokens: int = 1800
    timeout_seconds: int = 120
    site_url: str | None = None
    site_name: str | None = None
    system_prompt: str = DEFAULT_SYSTEM_PROMPT
    user_prompt: str = DEFAULT_USER_PROMPT
    image_detail: str = "high"
    image_encoding: str = "data_url"


@dataclass(frozen=True)
class VLMInferenceResult:
    sample_id: str
    model: str
    raw_text: str
    cadquery_code: str
    finish_reason: str | None
    usage: dict[str, Any] | None
    response_id: str | None
    latency_seconds: float
    output_path: str | None = None


@dataclass(frozen=True)
class BatchInferenceConfig:
    model: str = "openai/gpt-4o"
    temperature: float = 0.0
    max_tokens: int = 1800
    timeout_seconds: int = 120
    image_detail: str = "high"
    image_encoding: str = "data_url"
    system_prompt: str = DEFAULT_SYSTEM_PROMPT
    user_prompt: str = DEFAULT_USER_PROMPT
    output_root: str = "generated"
    retry_attempts: int = 5
    retry_base_delay_seconds: float = 2.0
    retry_max_delay_seconds: float = 30.0
    inter_request_delay_seconds: float = 0.0
    overwrite: bool = False
    write_code_outputs: bool = True


class OpenRouterClient:
    """
    Minimal OpenRouter client using the OpenAI-compatible chat completions endpoint.

    Endpoint is `POST https://openrouter.ai/api/v1/chat/completions`.
    """

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str = "https://openrouter.ai/api/v1",
        app_name: str | None = None,
        app_url: str | None = None,
    ) -> None:
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("Missing OpenRouter API key. Set OPENROUTER_API_KEY or pass api_key=...")
        self.base_url = base_url.rstrip("/")
        self.app_name = app_name
        self.app_url = app_url

    def chat_completions(self, body: dict[str, Any], timeout_seconds: int = 120) -> dict[str, Any]:
        url = f"{self.base_url}/chat/completions"
        data = json.dumps(body).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        if self.app_url:
            headers["HTTP-Referer"] = self.app_url
        if self.app_name:
            headers["X-Title"] = self.app_name

        request = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            err_body = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"OpenRouter HTTP {exc.code}: {err_body}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"OpenRouter request failed: {exc}") from exc

    def infer_cadquery_from_sample(
        self,
        dataset: CADDrawingDataset,
        sample: DrawingSample,
        config: VLMInferenceConfig | None = None,
        output_dir: str | Path | None = None,
        dry_run: bool = False,
    ) -> VLMInferenceResult | dict[str, Any]:
        cfg = config or VLMInferenceConfig()
        user_content = dataset.build_openai_vision_content(
            sample=sample,
            prompt=cfg.user_prompt,
            image_encoding=cfg.image_encoding,  # type: ignore[arg-type]
            image_detail=cfg.image_detail,
        )
        request_body: dict[str, Any] = {
            "model": cfg.model,
            "messages": [
                {"role": "system", "content": cfg.system_prompt},
                {"role": "user", "content": user_content},
            ],
            "temperature": cfg.temperature,
            "max_tokens": cfg.max_tokens,
        }

        if dry_run:
            return request_body

        t0 = time.perf_counter()
        response = self.chat_completions(request_body, timeout_seconds=cfg.timeout_seconds)
        latency = time.perf_counter() - t0

        raw_text = _extract_message_text(response)
        code = extract_cadquery_code(raw_text)
        output_path = None
        if output_dir is not None:
            output_path = str(write_inference_artifacts(output_dir, sample, cfg, response, code))

        choice0 = (response.get("choices") or [{}])[0]
        return VLMInferenceResult(
            sample_id=sample.sample_id,
            model=cfg.model,
            raw_text=raw_text,
            cadquery_code=code,
            finish_reason=choice0.get("finish_reason"),
            usage=response.get("usage"),
            response_id=response.get("id"),
            latency_seconds=latency,
            output_path=output_path,
        )

    def infer_cadquery_from_sample_with_retry(
        self,
        dataset: CADDrawingDataset,
        sample: DrawingSample,
        config: VLMInferenceConfig | None = None,
        output_dir: str | Path | None = None,
        retry_attempts: int = 5,
        retry_base_delay_seconds: float = 2.0,
        retry_max_delay_seconds: float = 30.0,
    ) -> VLMInferenceResult:
        cfg = config or VLMInferenceConfig()
        last_exc: Exception | None = None
        for attempt in range(1, retry_attempts + 1):
            try:
                result = self.infer_cadquery_from_sample(
                    dataset=dataset,
                    sample=sample,
                    config=cfg,
                    output_dir=output_dir,
                    dry_run=False,
                )
                assert isinstance(result, VLMInferenceResult)
                return result
            except Exception as exc:  # retry on transient OpenRouter/network/server issues
                last_exc = exc
                if attempt >= retry_attempts or not _is_retryable_error(exc):
                    raise
                sleep_s = min(retry_max_delay_seconds, retry_base_delay_seconds * (2 ** (attempt - 1)))
                time.sleep(sleep_s)
        assert last_exc is not None
        raise last_exc


def write_inference_artifacts(
    output_dir: str | Path,
    sample: DrawingSample,
    config: VLMInferenceConfig,
    response_json: dict[str, Any],
    cadquery_code: str,
) -> Path:
    out_dir = Path(output_dir) / sample.sample_id
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "response.json").write_text(
        json.dumps(response_json, indent=2, ensure_ascii=True),
        encoding="utf-8",
    )
    (out_dir / "cadquery.py").write_text(cadquery_code, encoding="utf-8")
    (out_dir / "request_config.json").write_text(
        json.dumps(asdict(config), indent=2, ensure_ascii=True),
        encoding="utf-8",
    )
    return out_dir


def run_batch_inference(
    dataset: CADDrawingDataset,
    client: OpenRouterClient,
    config: BatchInferenceConfig,
    sample_ids: list[str] | None = None,
) -> dict[str, Any]:
    model_dir = Path(config.output_root) / model_slug_to_dirname(config.model)
    model_dir.mkdir(parents=True, exist_ok=True)

    samples = dataset.list_samples()
    if sample_ids is not None:
        wanted = set(sample_ids)
        samples = [s for s in samples if s.sample_id in wanted]

    vlm_cfg = VLMInferenceConfig(
        model=config.model,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
        timeout_seconds=config.timeout_seconds,
        image_detail=config.image_detail,
        image_encoding=config.image_encoding,
        system_prompt=config.system_prompt,
        user_prompt=config.user_prompt,
    )

    summary: dict[str, Any] = {
        "model": config.model,
        "model_dir": str(model_dir),
        "mode": "batch" if config.write_code_outputs else "benchmark",
        "started_at": datetime.now(timezone.utc).isoformat(),
        "total": len(samples),
        "succeeded": 0,
        "skipped": 0,
        "failed": 0,
        "results": [],
    }

    for idx, sample in enumerate(samples, start=1):
        out_py = model_dir / f"{sample.stem}.py"
        record: dict[str, Any] = {
            "index": idx,
            "sample_id": sample.sample_id,
            "drawing_path": sample.drawing_path,
            "output_path": str(out_py) if config.write_code_outputs else None,
            "status": None,
        }

        if config.write_code_outputs and out_py.exists() and not config.overwrite:
            record["status"] = "skipped_exists"
            summary["skipped"] += 1
            summary["results"].append(record)
            continue

        try:
            result = client.infer_cadquery_from_sample_with_retry(
                dataset=dataset,
                sample=sample,
                config=vlm_cfg,
                output_dir=None,
                retry_attempts=config.retry_attempts,
                retry_base_delay_seconds=config.retry_base_delay_seconds,
                retry_max_delay_seconds=config.retry_max_delay_seconds,
            )
            if config.write_code_outputs:
                _write_generated_code_file(out_py, result.cadquery_code, config.model)
            record.update(
                {
                    "status": "ok",
                    "latency_seconds": result.latency_seconds,
                    "response_id": result.response_id,
                    "finish_reason": result.finish_reason,
                    "usage": result.usage,
                }
            )
            summary["succeeded"] += 1
        except Exception as exc:
            record.update({"status": "error", "error": str(exc)})
            summary["failed"] += 1

        summary["results"].append(record)

        if config.inter_request_delay_seconds > 0 and idx < len(samples):
            time.sleep(config.inter_request_delay_seconds)

    summary.update(_compute_benchmark_aggregates(summary["results"]))
    summary["finished_at"] = datetime.now(timezone.utc).isoformat()
    summary_path = model_dir / ("_batch_summary.json" if config.write_code_outputs else "_benchmark_summary.json")
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=True), encoding="utf-8")
    summary["summary_path"] = str(summary_path)
    return summary


def extract_cadquery_code(text: str) -> str:
    """
    Extract Python code from a model response.

    Preference order:
    1. ```python fenced block
    2. any fenced block
    3. raw text
    """
    fenced_python = re.findall(r"```python\s*(.*?)```", text, flags=re.IGNORECASE | re.DOTALL)
    if fenced_python:
        return fenced_python[0].strip() + "\n"

    fenced_any = re.findall(r"```\s*(.*?)```", text, flags=re.DOTALL)
    if fenced_any:
        return fenced_any[0].strip() + "\n"

    return text.strip() + ("\n" if text.strip() else "")


def model_slug_to_dirname(model: str) -> str:
    # User asked for e.g. `gpt-4o` instead of `openai/gpt-4o`.
    return model.split("/")[-1].strip() or "model"


def _write_generated_code_file(path: Path, code: str, model: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    header = f"# model used: {model}\n"
    body = code.lstrip("\ufeff")
    if body.startswith("# model used:") or body.startswith("# model:"):
        # Replace any model header emitted by previous runs/model responses.
        body = "\n".join(body.splitlines()[1:]).lstrip("\n")
    path.write_text(header + body, encoding="utf-8")


def _extract_message_text(response_json: dict[str, Any]) -> str:
    choices = response_json.get("choices") or []
    if not choices:
        return ""
    message = choices[0].get("message") or {}
    content = message.get("content")

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, dict):
                if item.get("type") in {"text", "output_text"} and isinstance(item.get("text"), str):
                    parts.append(item["text"])
                elif isinstance(item.get("content"), str):
                    parts.append(item["content"])
        return "\n".join(p for p in parts if p)

    return str(content) if content is not None else ""


def _is_retryable_error(exc: Exception) -> bool:
    msg = str(exc).lower()
    retry_markers = [
        "http 429",
        "rate limit",
        "too many requests",
        "http 500",
        "http 502",
        "http 503",
        "http 504",
        "timed out",
        "timeout",
        "temporar",
        "connection reset",
        "connection refused",
    ]
    return any(marker in msg for marker in retry_markers)


def _compute_benchmark_aggregates(results: list[dict[str, Any]]) -> dict[str, Any]:
    ok_rows = [r for r in results if r.get("status") == "ok"]
    latencies = [float(r["latency_seconds"]) for r in ok_rows if isinstance(r.get("latency_seconds"), (int, float))]
    aggregate: dict[str, Any] = {
        "benchmark": {
            "n_ok": len(ok_rows),
            "n_error": len([r for r in results if r.get("status") == "error"]),
            "latency_seconds": None,
            "usage_totals": {},
            "usage_averages_per_ok": {},
        }
    }

    if latencies:
        lat_sorted = sorted(latencies)
        n = len(lat_sorted)
        aggregate["benchmark"]["latency_seconds"] = {
            "min": lat_sorted[0],
            "max": lat_sorted[-1],
            "mean": sum(lat_sorted) / n,
            "median": lat_sorted[n // 2] if n % 2 == 1 else (lat_sorted[n // 2 - 1] + lat_sorted[n // 2]) / 2.0,
        }

    usage_totals: dict[str, float] = {}
    for row in ok_rows:
        usage = row.get("usage")
        if not isinstance(usage, dict):
            continue
        for key, value in usage.items():
            if isinstance(value, (int, float)):
                usage_totals[key] = usage_totals.get(key, 0.0) + float(value)

    if usage_totals:
        aggregate["benchmark"]["usage_totals"] = usage_totals
        n_ok = max(1, len(ok_rows))
        aggregate["benchmark"]["usage_averages_per_ok"] = {
            k: v / n_ok for k, v in usage_totals.items()
        }

    return aggregate
