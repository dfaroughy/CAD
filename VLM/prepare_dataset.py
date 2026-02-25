from __future__ import annotations

import argparse
import json
from pathlib import Path

from .dataset import CADDrawingDataset, samples_to_dicts


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare CAD drawing image dataset metadata for VLM inference.")
    parser.add_argument("--repo-root", default=".", help="Repository root (default: current directory)")
    parser.add_argument("--drawings-dir", default="data/drawings", help="Relative drawings directory")
    parser.add_argument("--models-dir", default="data/models", help="Relative models directory")
    parser.add_argument("--manifest-jsonl", default=None, help="Optional output path for JSONL manifest")
    parser.add_argument("--limit", type=int, default=None, help="Optional sample limit")
    parser.add_argument(
        "--print-json",
        action="store_true",
        help="Print JSON preview to stdout instead of only summary.",
    )
    args = parser.parse_args()

    ds = CADDrawingDataset(
        repo_root=args.repo_root,
        drawings_dir=args.drawings_dir,
        models_dir=args.models_dir,
    )

    samples = ds.list_samples()
    if args.limit is not None:
        samples = samples[: args.limit]

    if args.manifest_jsonl:
        manifest_path = Path(args.manifest_jsonl)
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        with manifest_path.open("w", encoding="utf-8") as f:
            for sample in samples:
                f.write(json.dumps(sample.__dict__, ensure_ascii=True) + "\n")

    if args.print_json:
        print(json.dumps(samples_to_dicts(samples), indent=2))
    else:
        print(f"samples={len(samples)} drawings_dir={ds.drawings_dir}")
        if samples:
            first = samples[0]
            print(
                f"example={first.sample_id} mime={first.mime_type} size={first.width}x{first.height} "
                f"paired_model={'yes' if first.model_path else 'no'}"
            )


if __name__ == "__main__":
    main()
