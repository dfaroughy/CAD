from __future__ import annotations

import argparse
import csv
import json
import math
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

IMPORT_ERROR: Exception | None = None
try:
    from metrics import (
        code_runs,
        combined_pvalue,
        point_cloud_dist,
        shape_volume_dist,
        two_point_corr_dist,
    )
    from utils import _extract_cad_model
except Exception as exc:
    IMPORT_ERROR = exc
    code_runs = None  # type: ignore[assignment]
    combined_pvalue = None  # type: ignore[assignment]
    point_cloud_dist = None  # type: ignore[assignment]
    shape_volume_dist = None  # type: ignore[assignment]
    two_point_corr_dist = None  # type: ignore[assignment]
    _extract_cad_model = None  # type: ignore[assignment]


def load_workplane(py_path: Path):
    if IMPORT_ERROR is not None:
        raise RuntimeError(_dependency_error_message()) from IMPORT_ERROR
    return _extract_cad_model(str(py_path), output="workplane")


def compare_pair(
    generated_path: Path,
    truth_path: Path,
    tol: float,
    n_bins_xi: int,
    n_bins_pv: int,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "sample_id": generated_path.stem,
        "generated_path": str(generated_path),
        "truth_path": str(truth_path),
        "status": "ok",
    }

    # --- code-level check on the generated file ---
    cr = code_runs(str(generated_path))
    row["code_runs"] = {
        "success":    cr["success"],
        "n_steps_ok": cr["n_steps_ok"],
        "has_result": cr["has_result"],
        "error_type": cr.get("error_type"),
        "error_msg":  cr.get("error_msg"),
    }
    if not cr["success"]:
        row["status"] = "code_error"
        return row

    # --- load both workplanes ---
    try:
        gen_obj = load_workplane(generated_path)
    except Exception as exc:
        row.update({"status": "generated_load_error", "error": f"{type(exc).__name__}: {exc}",
                    "traceback": traceback.format_exc(limit=5)})
        return row

    if gen_obj is None:
        row.update({"status": "generated_load_error", "error": "workplane is None after exec"})
        return row

    try:
        truth_obj = load_workplane(truth_path)
    except Exception as exc:
        row.update({"status": "truth_load_error", "error": f"{type(exc).__name__}: {exc}",
                    "traceback": traceback.format_exc(limit=5)})
        return row

    if truth_obj is None:
        row.update({"status": "truth_load_error", "error": "workplane is None after exec"})
        return row

    # --- shape metrics (mirrors results() in metrics.py) ---
    try:
        vol_rel  = shape_volume_dist(truth_obj, gen_obj)["rel_diff"]
        hausdorff = point_cloud_dist(truth_obj, gen_obj, tol=tol)["hausdorff"]
        xi_l2    = two_point_corr_dist(truth_obj, gen_obj, tol=tol, n_bins=n_bins_xi)["l2"]
        pv       = combined_pvalue(truth_obj, gen_obj, tol=tol, n_bins=n_bins_pv)

        row["metrics"] = {
            "vol_rel":   vol_rel,
            "hausdorff": hausdorff,
            "xi_l2":     xi_l2,
            "p_value":   pv["p_value"],
            "p_pc":      pv["p_pc"],
            "p_xi":      pv["p_xi"],
            "z_hausdorff": pv["z_scores"]["hausdorff"],
            "z_chamfer":   pv["z_scores"]["chamfer"],
        }
    except Exception as exc:
        row.update({"status": "metrics_error", "error": f"{type(exc).__name__}: {exc}",
                    "traceback": traceback.format_exc(limit=5)})
    return row


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    ok_rows = [r for r in rows if r.get("status") == "ok"]
    summary: dict[str, Any] = {
        "total":         len(rows),
        "ok":            len(ok_rows),
        "failed":        len(rows) - len(ok_rows),
        "status_counts": {},
        "aggregates":    {},
    }
    for r in rows:
        s = r.get("status", "unknown")
        summary["status_counts"][s] = summary["status_counts"].get(s, 0) + 1

    metric_keys = ["vol_rel", "hausdorff", "xi_l2", "p_value"]
    values: dict[str, list[float]] = {k: [] for k in metric_keys}
    for r in ok_rows:
        m = r.get("metrics") or {}
        for k in metric_keys:
            v = m.get(k)
            if isinstance(v, (int, float)) and math.isfinite(float(v)):
                values[k].append(float(v))

    for k, arr in values.items():
        if not arr:
            continue
        arr_s = sorted(arr)
        n = len(arr_s)
        summary["aggregates"][k] = {
            "mean":   sum(arr_s) / n,
            "median": arr_s[n // 2] if n % 2 else (arr_s[n // 2 - 1] + arr_s[n // 2]) / 2.0,
            "min":    arr_s[0],
            "max":    arr_s[-1],
        }
    return summary


METRIC_KEYS = ["vol_rel", "hausdorff", "xi_l2", "p_value", "p_pc", "p_xi", "z_hausdorff", "z_chamfer"]
CSV_FIELDS  = ["sample_id", "status"] + METRIC_KEYS + ["code_success", "code_error_type", "code_error_msg",
                                                         "generated_path", "truth_path", "error"]


def write_csv(rows: list[dict[str, Any]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for r in rows:
            m  = r.get("metrics") or {}
            cr = r.get("code_runs") or {}
            writer.writerow({
                "sample_id":      r.get("sample_id"),
                "status":         r.get("status"),
                "generated_path": r.get("generated_path"),
                "truth_path":     r.get("truth_path"),
                "error":          r.get("error"),
                "code_success":   cr.get("success"),
                "code_error_type": cr.get("error_type"),
                "code_error_msg":  cr.get("error_msg"),
                **{k: m.get(k) for k in METRIC_KEYS},
            })


def run_one_model(
    generated_dir: Path,
    truth_dir: Path,
    output_dir: Path,
    tol: float,
    n_bins_xi: int,
    n_bins_pv: int,
    limit: int | None,
    skip_missing_truth: bool,
) -> dict[str, Any]:
    generated_files = sorted(p for p in generated_dir.glob("*.py") if p.is_file())
    if limit is not None:
        generated_files = generated_files[:limit]

    rows: list[dict[str, Any]] = []
    n = len(generated_files)
    for idx, gen_path in enumerate(generated_files, start=1):
        truth_path = truth_dir / gen_path.name
        if not truth_path.exists():
            if not skip_missing_truth:
                rows.append({"sample_id": gen_path.stem, "generated_path": str(gen_path),
                             "truth_path": str(truth_path), "status": "missing_truth"})
            continue
        row = compare_pair(gen_path, truth_path, tol=tol, n_bins_xi=n_bins_xi, n_bins_pv=n_bins_pv)
        row["index"] = idx
        rows.append(row)
        status = row["status"]
        metrics_str = ""
        if status == "ok":
            m = row.get("metrics", {})
            metrics_str = (f"  vol_rel={m.get('vol_rel', float('nan')):.3f}"
                           f"  haus={m.get('hausdorff', float('nan')):.3f}"
                           f"  xi_l2={m.get('xi_l2', float('nan')):.3f}"
                           f"  p={m.get('p_value', float('nan')):.3f}")
        print(f"  [{idx}/{n}] {gen_path.stem}: {status}{metrics_str}")

    summary = summarize(rows)
    result = {
        "model":         generated_dir.name,
        "generated_dir": str(generated_dir),
        "truth_dir":     str(truth_dir),
        "created_at":    datetime.now(timezone.utc).isoformat(),
        "config":        {"tol": tol, "n_bins_xi": n_bins_xi, "n_bins_pv": n_bins_pv, "limit": limit},
        "summary":       summary,
        "rows":          rows,
    }

    tag = generated_dir.name
    json_path = output_dir / f"compare_{tag}.json"
    csv_path  = output_dir / f"compare_{tag}.csv"
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(result, indent=2, ensure_ascii=True), encoding="utf-8")
    write_csv(rows, csv_path)
    print(f"  → ok={summary['ok']} code_error={summary['status_counts'].get('code_error', 0)}"
          f" failed={summary['failed']} total={summary['total']}")
    print(f"  → json={json_path}  csv={csv_path}")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare VLM-generated CadQuery scripts against ground truth using geometry metrics."
    )
    parser.add_argument("--generated-dir", default=None,
                        help="Folder with generated *.py files (single model). "
                             "Mutually exclusive with --all-models.")
    parser.add_argument("--all-models", action="store_true",
                        help="Run all model subdirectories found in --models-root.")
    parser.add_argument("--models-root", default="generated",
                        help="Parent folder containing per-model subdirs (used with --all-models).")
    parser.add_argument("--truth-dir", default="data/models",
                        help="Ground-truth CAD script folder.")
    parser.add_argument("--output-dir", default="Analysis/results",
                        help="Directory for JSON/CSV outputs.")
    parser.add_argument("--limit", type=int, default=None,
                        help="Optional max number of files per model.")
    parser.add_argument("--tol", type=float, default=0.05,
                        help="Tessellation tolerance.")
    parser.add_argument("--n-bins-xi", type=int, default=64,
                        help="Bins for the 2PCF xi(r) L2 metric.")
    parser.add_argument("--n-bins-pv", type=int, default=20,
                        help="Bins for the 2PCF component inside combined_pvalue.")
    parser.add_argument("--skip-missing-truth", action="store_true",
                        help="Skip generated files with no matching truth file.")
    args = parser.parse_args()

    if IMPORT_ERROR is not None:
        raise RuntimeError(_dependency_error_message()) from IMPORT_ERROR

    truth_dir  = Path(args.truth_dir)
    output_dir = Path(args.output_dir)

    if not truth_dir.exists():
        raise FileNotFoundError(f"Truth dir not found: {truth_dir}")

    if args.all_models:
        models_root = Path(args.models_root)
        if not models_root.exists():
            raise FileNotFoundError(f"Models root not found: {models_root}")
        model_dirs = sorted(p for p in models_root.iterdir() if p.is_dir())
        if not model_dirs:
            raise FileNotFoundError(f"No subdirectories found in {models_root}")
        all_results = {}
        for gen_dir in model_dirs:
            print(f"\n=== {gen_dir.name} ===")
            all_results[gen_dir.name] = run_one_model(
                gen_dir, truth_dir, output_dir,
                tol=args.tol, n_bins_xi=args.n_bins_xi, n_bins_pv=args.n_bins_pv,
                limit=args.limit, skip_missing_truth=args.skip_missing_truth,
            )
        # combined summary JSON
        combined_path = output_dir / "compare_all_models.json"
        combined_path.write_text(
            json.dumps({m: r["summary"] for m, r in all_results.items()}, indent=2),
            encoding="utf-8",
        )
        print(f"\nCombined summary → {combined_path}")
    else:
        if args.generated_dir is None:
            parser.error("Provide --generated-dir or --all-models.")
        gen_dir = Path(args.generated_dir)
        if not gen_dir.exists():
            raise FileNotFoundError(f"Generated dir not found: {gen_dir}")
        run_one_model(
            gen_dir, truth_dir, output_dir,
            tol=args.tol, n_bins_xi=args.n_bins_xi, n_bins_pv=args.n_bins_pv,
            limit=args.limit, skip_missing_truth=args.skip_missing_truth,
        )


def _dependency_error_message() -> str:
    return (
        "Failed to import CAD metrics dependencies. This script requires a working CadQuery "
        "environment. Detected import error (often cadquery/pyparsing mismatch). "
        "Try fixing the active env and rerun."
    )


if __name__ == "__main__":
    main()
