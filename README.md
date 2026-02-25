# CAD VLM Benchmark

Evaluate vision-language models on their ability to reconstruct CadQuery 3-D models from 2-D engineering drawings.

## Pipeline overview

```
data/drawings/   (PNG images)
      │
      ▼
VLM inference  →  generated/<model>/*.py
      │
      ▼
Analysis       →  Analysis/results/compare_<model>.csv / .json
                  Analysis/results/view_comparison/<object>.png
```

---

## 1  Run inference

Requires an `OPENROUTER_API_KEY` environment variable.

```bash
# Built-in preset
python -m VLM.run_batch_inference --repo-root . --model gpt-4o

# Any OpenRouter slug (e.g. the new Llama 4 Maverick)
python -m VLM.run_batch_inference --repo-root . --model meta-llama/llama-4-maverick

# List available built-in presets
python -m VLM.run_batch_inference --list-models
```

**Built-in presets**

| Preset | Model |
|---|---|
| `gpt-4o` | openai/gpt-4o |
| `claude-3.5-sonnet` | anthropic/claude-3.5-sonnet |
| `qwen2.5-vl-72b` | qwen/qwen2.5-vl-72b-instruct |
| `gemma-3` | google/gemma-3-27b-it |
| `llama-3.2-vision` | meta-llama/llama-3.2-90b-vision-instruct |

Any raw OpenRouter slug not in the table is also accepted directly.

**Useful flags**

| Flag | Default | Description |
|---|---|---|
| `--limit N` | all | Process only the first N samples |
| `--start-index N` | 0 | Skip the first N samples |
| `--overwrite` | off | Re-generate files that already exist |
| `--dry-run` | off | Print what would run without calling the API |
| `--temperature` | 0.0 | Sampling temperature |
| `--max-tokens` | 1800 | Max output tokens |

Output is written to `generated/<model_name>/` as one `.py` file per drawing.

---

## 2  Compute metrics

Compares each generated file against the matching ground-truth model in `data/models/`.
Metrics per sample: `vol_rel`, `hausdorff`, `xi_l2`, `p_value` (Fisher combined).

```bash
# All models at once → Analysis/results/compare_<model>.csv + compare_all_models.json
python Analysis/compare_generated_to_truth.py --all-models

# Single model
python Analysis/compare_generated_to_truth.py --generated-dir generated/gpt-4o

# Quick test (first 5 samples)
python Analysis/compare_generated_to_truth.py --all-models --limit 5
```

Files that fail to execute are recorded as `code_error` rows; shape metrics are only
computed for files that run successfully.

---

## 3  Render visual comparison

Produces one PNG per object: ground-truth build steps in the top row, each VLM model
in the rows below.

```bash
# All objects → Analysis/results/view_comparison/*.png
python Analysis/render_comparison.py

# Quick test (first 5 objects)
python Analysis/render_comparison.py --limit 5

# Single object
python Analysis/render_comparison.py --stem 20251218_033650_brass_spacer_tube_v1
```

---

## 4  Evaluation notebook

Open `notebooks/evaluation.ipynb` after running step 2.  Requires the CSVs in
`Analysis/results/`.

Sections:
- **Leaderboard** — per-model mean/median of all four metrics + code pass rate
- **Box plots** — metric distributions across models
- **Scatter** — code pass rate vs shape quality
- **Error breakdown** — failure type breakdown per model (`SyntaxError`, `ValueError`, …)
- **Per-sample inspection** — best / worst shapes by Hausdorff distance
