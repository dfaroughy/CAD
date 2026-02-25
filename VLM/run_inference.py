from __future__ import annotations

import argparse
import json

from .dataset import CADDrawingDataset
from .inference import OpenRouterClient, VLMInferenceConfig, VLMInferenceResult
from .models import list_model_presets, resolve_model_slug


def main() -> None:
    parser = argparse.ArgumentParser(description="Run VLM CAD inference on drawing images via OpenRouter.")
    parser.add_argument("--repo-root", default=".", help="Repository root")
    parser.add_argument("--sample-id", default=None, help="Specific sample_id to run (default: first sample)")
    parser.add_argument("--model", default="gpt-4o", help="Model preset name or OpenRouter model slug")
    parser.add_argument("--temperature", type=float, default=0.0, help="Sampling temperature")
    parser.add_argument("--max-tokens", type=int, default=1800, help="Max completion tokens")
    parser.add_argument("--timeout", type=int, default=120, help="HTTP timeout seconds")
    parser.add_argument("--output-dir", default="VLM/outputs", help="Where to save response/code artifacts")
    parser.add_argument(
        "--image-detail",
        default="high",
        choices=["low", "high", "auto"],
        help="OpenAI-compatible image detail hint",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print request JSON without calling the API",
    )
    parser.add_argument(
        "--dry-run-full",
        action="store_true",
        help="With --dry-run, print the full base64 image payload instead of a redacted preview",
    )
    parser.add_argument(
        "--print-raw",
        action="store_true",
        help="Print raw model text response in addition to extracted code summary",
    )
    parser.add_argument("--list-models", action="store_true", help="List built-in model presets and exit")
    args = parser.parse_args()

    if args.list_models:
        for p in list_model_presets():
            kind = "open" if p.open_source else "closed"
            print(f"{p.name:18} -> {p.slug} [{kind}]")
        return

    ds = CADDrawingDataset(args.repo_root)
    sample = ds.get_sample(args.sample_id) if args.sample_id else ds.list_samples()[0]
    model_slug = resolve_model_slug(args.model)

    cfg = VLMInferenceConfig(
        model=model_slug,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        timeout_seconds=args.timeout,
        image_detail=args.image_detail,
    )

    if args.dry_run:
        content = ds.build_openai_vision_content(
            sample=sample,
            prompt=cfg.user_prompt,
            image_encoding=cfg.image_encoding,  # type: ignore[arg-type]
            image_detail=cfg.image_detail,
        )
        request_body = {
            "model": cfg.model,
            "messages": [
                {"role": "system", "content": cfg.system_prompt},
                {"role": "user", "content": content},
            ],
            "temperature": cfg.temperature,
            "max_tokens": cfg.max_tokens,
        }
        if not args.dry_run_full:
            request_body = _redact_image_data_urls(request_body)
        print(json.dumps(request_body, indent=2, ensure_ascii=True))
        return

    client = OpenRouterClient()
    result = client.infer_cadquery_from_sample(
        dataset=ds,
        sample=sample,
        config=cfg,
        output_dir=args.output_dir,
        dry_run=False,
    )

    assert isinstance(result, VLMInferenceResult)
    print(f"sample_id={result.sample_id}")
    print(f"model={result.model}")
    print(f"latency_seconds={result.latency_seconds:.2f}")
    print(f"finish_reason={result.finish_reason}")
    print(f"response_id={result.response_id}")
    if result.usage:
        print("usage=" + json.dumps(result.usage, ensure_ascii=True))
    if result.output_path:
        print(f"output_path={result.output_path}")
    print("cadquery_code_preview:")
    print(result.cadquery_code[:1000])
    if args.print_raw:
        print("\nraw_text:")
        print(result.raw_text)


def _redact_image_data_urls(obj):
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k == "url" and isinstance(v, str) and v.startswith("data:image/"):
                prefix, _, payload = v.partition(",")
                preview = payload[:80] + ("..." if len(payload) > 80 else "")
                out[k] = f"{prefix},<base64:{len(payload)} chars preview={preview}>"
            else:
                out[k] = _redact_image_data_urls(v)
        return out
    if isinstance(obj, list):
        return [_redact_image_data_urls(x) for x in obj]
    return obj


if __name__ == "__main__":
    main()
