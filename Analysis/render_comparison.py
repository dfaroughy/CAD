"""
Render side-by-side step comparisons: ground truth (top row) vs VLM models (rows below).

Columns  = CadQuery build steps (step1, step2, …, result) taken from the truth model.
Rows     = ground truth  +  one row per VLM model whose file exists for this object.
Output   = Analysis/results/view_comparison/<object_stem>.png

Usage
-----
# All objects
python Analysis/render_comparison.py

# Quick test: first 5 objects
python Analysis/render_comparison.py --limit 5

# Single object
python Analysis/render_comparison.py --stem 20251218_033650_brass_spacer_tube_v1
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")          # non-interactive, safe for scripts
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from utils import cad_model_seq

MODELS = [
    "gpt-4o",
    "claude-3.5-sonnet",
    "gemma-3-27b-it",
    "qwen2.5-vl-72b-instruct",
]
TRUTH_DIR = REPO_ROOT / "data" / "models"
GEN_ROOT  = REPO_ROOT / "generated"
OUT_DIR   = REPO_ROOT / "Analysis" / "results" / "view_comparison"

# ── rendering ────────────────────────────────────────────────────────────────

def _render_obj(ax, obj) -> None:
    """Draw a CadQuery Workplane into a 3-D axes, or show an error label.
    Rendering params match show_3d() in utils.py."""
    ax.set_axis_off()
    if obj is None:
        ax.text2D(0.5, 0.5, "failed", ha="center", va="center",
                  transform=ax.transAxes, color="#c0392b",
                  fontsize=11, fontweight="bold")
        return
    try:
        vertices, triangles = obj.val().tessellate(0.01)
        if not vertices or not triangles:
            raise ValueError("empty tessellation")
        verts = [[[vertices[i].x, vertices[i].y, vertices[i].z] for i in tri]
                 for tri in triangles]
        poly = Poly3DCollection(verts, alpha=0.1, linewidth=0.2, edgecolor="k")
        poly.set_facecolor(None)
        ax.add_collection3d(poly)

        pts = np.array([[v.x, v.y, v.z] for v in vertices])
        ax.set_xlim(pts[:, 0].min(), pts[:, 0].max())
        ax.set_ylim(pts[:, 1].min(), pts[:, 1].max())
        ax.set_zlim(pts[:, 2].min(), pts[:, 2].max())
    except Exception:
        ax.text2D(0.5, 0.5, "render\nerror", ha="center", va="center",
                  transform=ax.transAxes, color="#e67e22", fontsize=9)


# ── step ordering ─────────────────────────────────────────────────────────────

def _step_keys(steps: dict) -> list[str]:
    """['step1', 'step2', …, 'result'] in numerical order."""
    numeric = sorted(
        (k for k in steps if k.startswith("step") and k[4:].isdigit()),
        key=lambda s: int(s[4:]),
    )
    return numeric + (["result"] if "result" in steps else [])


# ── figure builder ────────────────────────────────────────────────────────────

def _make_figure(
    stem: str,
    truth_steps: dict,
    model_steps: dict[str, dict | None],   # model_name -> steps dict or None
) -> plt.Figure | None:
    cols = _step_keys(truth_steps)
    if not cols:
        return None

    n_cols = len(cols)
    # Only rows where the generated file exists (even if code failed → steps is {})
    present = {m: s for m, s in model_steps.items() if s is not None}
    row_labels = ["ground truth"] + list(present.keys())
    n_rows = len(row_labels)

    cell_w, cell_h = 2.8, 2.8
    fig, axes = plt.subplots(
        n_rows, n_cols,
        figsize=(cell_w * n_cols, cell_h * n_rows),
        subplot_kw={"projection": "3d"},
        squeeze=False,
    )

    # ── column headers (step names) on the top-row axes ──
    for j, col in enumerate(cols):
        axes[0, j].set_title(col, fontsize=10, fontweight="bold",
                              pad=2, color="#333333")

    # ── render truth ──
    for j, col in enumerate(cols):
        _render_obj(axes[0, j], truth_steps.get(col))

    # ── render each model row ──
    for i, model in enumerate(row_labels[1:], start=1):
        steps = present[model]
        for j, col in enumerate(cols):
            _render_obj(axes[i, j], steps.get(col) if steps else None)

    # ── row labels (added after tight_layout so positions are accurate) ──
    fig.suptitle(stem.replace("_", " "), fontsize=11, fontweight="bold")
    plt.tight_layout(pad=0.5, rect=[0.10, 0, 1, 0.97])

    for i, (row_axes, label) in enumerate(zip(axes, row_labels)):
        pos   = row_axes[0].get_position()           # figure-fraction bbox
        y_mid = (pos.y0 + pos.y1) / 2
        short = label if label == "ground truth" else label.split("/")[-1]
        # font size scales down a bit for long names
        fs = 9 if len(short) <= 14 else 7
        fig.text(0.005, y_mid, short,
                 ha="left", va="center",
                 fontsize=fs, fontweight="bold", color="#111111",
                 rotation=90 if len(short) > 20 else 0)

    return fig


# ── per-object entry point ────────────────────────────────────────────────────

def process_one(
    truth_path: Path,
    models: list[str],
    gen_root: Path,
    out_dir: Path,
) -> None:
    stem = truth_path.stem
    truth_steps = cad_model_seq(str(truth_path))

    model_steps: dict[str, dict | None] = {}
    for model in models:
        gen_path = gen_root / model / truth_path.name
        if gen_path.exists():
            model_steps[model] = cad_model_seq(str(gen_path))
        # else: file absent for this model → don't include row

    fig = _make_figure(stem, truth_steps, model_steps)
    if fig is None:
        print(f"  {stem}: nothing to render")
        return

    out_path = out_dir / f"{stem}.png"
    fig.savefig(str(out_path), dpi=130, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  → {out_path.name}")


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render step-by-step 3-D comparison PNGs for each CAD object."
    )
    parser.add_argument("--truth-dir", default=str(TRUTH_DIR))
    parser.add_argument("--gen-root",  default=str(GEN_ROOT))
    parser.add_argument("--out-dir",   default=str(OUT_DIR))
    parser.add_argument("--limit",     type=int, default=None,
                        help="Process only the first N objects.")
    parser.add_argument("--stem",      default=None,
                        help="Process a single object by its stem name.")
    args = parser.parse_args()

    truth_dir = Path(args.truth_dir)
    gen_root  = Path(args.gen_root)
    out_dir   = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(truth_dir.glob("*.py"))
    if args.stem:
        files = [f for f in files if f.stem == args.stem]
    if args.limit:
        files = files[: args.limit]

    print(f"Rendering {len(files)} object(s) → {out_dir}")
    for truth_path in files:
        print(f"[{truth_path.stem}]")
        process_one(truth_path, MODELS, gen_root, out_dir)


if __name__ == "__main__":
    main()
