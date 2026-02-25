from __future__ import annotations

import argparse
import json

from .dataset import CADDrawingDataset
from .inference import BatchInferenceConfig, OpenRouterClient, run_batch_inference
from .models import list_model_presets, resolve_model_slug


def main() -> None:
    parser = argparse.ArgumentParser(description="Batch VLM CAD inference over data/drawings via OpenRouter.")
    parser.add_argument("--repo-root", default=".", help="Repository root")
    parser.add_argument("--drawings-dir", default="data/drawings", help="Drawings directory")
    parser.add_argument("--models-dir", default="data/models", help="Models directory")
    parser.add_argument("--model", default="gpt-4o", help="Model preset name or OpenRouter model slug")
    parser.add_argument("--output-root", default="generated", help="Output root; files go to generated/<model_name>/")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max-tokens", type=int, default=1800)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--image-detail", choices=["low", "high", "auto"], default="high")
    parser.add_argument("--retry-attempts", type=int, default=5)
    parser.add_argument("--retry-base-delay", type=float, default=2.0)
    parser.add_argument("--retry-max-delay", type=float, default=30.0)
    parser.add_argument("--inter-request-delay", type=float, default=0.0)
    parser.add_argument("--limit", type=int, default=None, help="Only process first N samples")
    parser.add_argument("--start-index", type=int, default=0, help="0-based start index in sorted samples")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing generated .py files")
    parser.add_argument("--dry-run", action="store_true", help="Print selected sample IDs and exit")
    parser.add_argument("--list-models", action="store_true", help="List built-in model presets and exit")
    parser.add_argument(
        "--benchmark",
        action="store_true",
        help="Benchmark mode: run inference and collect latency/usage stats without writing per-sample .py outputs",
    )
    args = parser.parse_args()

    if args.list_models:
        for p in list_model_presets():
            kind = "open" if p.open_source else "closed"
            print(f"{p.name:18} -> {p.slug} [{kind}]")
        return

    ds = CADDrawingDataset(
        repo_root=args.repo_root,
        drawings_dir=args.drawings_dir,
        models_dir=args.models_dir,
    )
    samples = ds.list_samples()
    selected = samples[args.start_index :]
    if args.limit is not None:
        selected = selected[: args.limit]
    sample_ids = [s.sample_id for s in selected]

    model_slug = resolve_model_slug(args.model)

    if args.dry_run:
        print(
            json.dumps(
                {
                    "count": len(sample_ids),
                    "model_input": args.model,
                    "model_resolved": model_slug,
                    "mode": "benchmark" if args.benchmark else "batch",
                    "output_dir": f"{args.output_root}/{model_slug.split('/')[-1]}",
                    "sample_ids": sample_ids,
                },
                indent=2,
                ensure_ascii=True,
            )
        )
        return

    client = OpenRouterClient()
    cfg = BatchInferenceConfig(
        model=model_slug,
        output_root=args.output_root,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        timeout_seconds=args.timeout,
        image_detail=args.image_detail,
        retry_attempts=args.retry_attempts,
        retry_base_delay_seconds=args.retry_base_delay,
        retry_max_delay_seconds=args.retry_max_delay,
        inter_request_delay_seconds=args.inter_request_delay,
        overwrite=args.overwrite,
        write_code_outputs=not args.benchmark,
    )

    summary = run_batch_inference(
        dataset=ds,
        client=client,
        config=cfg,
        sample_ids=sample_ids,
    )

    print(f"model={summary['model']}")
    print(f"mode={summary.get('mode')}")
    print(f"model_dir={summary['model_dir']}")
    print(f"total={summary['total']} succeeded={summary['succeeded']} skipped={summary['skipped']} failed={summary['failed']}")
    print(f"summary_path={summary['summary_path']}")
    bench = summary.get("benchmark") or {}
    if bench:
        print("benchmark=" + json.dumps(bench, ensure_ascii=True))

    errors = [r for r in summary["results"] if r.get("status") == "error"]
    if errors:
        print("errors_preview:")
        for row in errors[:10]:
            print(f"- {row['sample_id']}: {row.get('error')}")


if __name__ == "__main__":
    main()
