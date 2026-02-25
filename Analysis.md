# Benchmark Analysis

## Results Summary

| Model | Code Pass | Median vol_rel | Median hausdorff | Median xi_l2 | p_value > 0 |
|---|---|---|---|---|---|
| **Qwen2.5-VL-72B** | **98%** | 0.43 | 26.65 | 43.21 | 0 / 98 |
| **GPT-4o** | 77% | **0.30** | **20.07** | **33.33** | 1 / 77 |
| Gemma-3-27B | 63% | 0.57 | 30.06 | 60.54 | 0 / 63 |
| Claude-3.5-Sonnet | 7% | 0.65 | 24.52 | 62.82 | 0 / 7 |

**On p_values:** essentially all are 0 across all models — the Fisher test is saturated, meaning every reconstructed shape is statistically distinguishable from ground truth. The only exception is one GPT-4o sample (`cube_with_beveled_corners`) which reaches p≈1 with hausdorff=0 and vol_rel=0 — a near-perfect reconstruction. The p_value is best treated as a "perfect match" detector rather than a graded similarity score; the continuous metrics (hausdorff, xi_l2) carry more information in the non-perfect regime.

---

## 1. Systematic Evaluation

**Models benchmarked:** GPT-4o (closed), Claude-3.5-Sonnet (closed), Qwen2.5-VL-72B (open), Gemma-3-27B-IT (open) — 100 engineering drawings each.

**Scoring criteria (in order of priority):**
1. **Code pass rate**: does the output execute at all? A prerequisite for everything else
2. **Hausdorff distance**: worst-case point-level deviation from ground truth surface (mm)
3. **vol_rel**: relative volume difference, catches gross scale/topology errors
4. **xi_l2**: Landy-Szalay 2PCF L2 norm, that is common in numerical cosmology and has the benefit of being invaraint under rotations and reflexions. This may be a new metric in this context? 
5. **p_value**: combined significance test saturates quickly, useful only if the model perfomred perfectly. 

**Verdict:** Qwen2.5-VL-72B is the most reliable model overall (98% code pass, competitive shape quality). GPT-4o produces the best shape quality among successful runs (median hausdorff 20.07 vs Qwen's 26.65, median xi_l2 33 vs 43) but drops 23% of samples at the code stage. Claude-3.5-Sonnet is disqualified from shape comparison by its 93% code failure rate — this is a configuration artifact, not a capability ceiling (see §2). No model achieves statistically equivalent reconstruction on any but the simplest geometry.

![alt text](image.png)


---

## 2. Failure Mode Analysis

**Two distinct failure layers:**

### Layer 1 — Code generation failures

| Model | Dominant error | Root cause |
|---|---|---|
| Claude-3.5-Sonnet | SyntaxError: *"unexpected EOF"*, *"'(' was never closed"* (77/92 failures) | **Truncation.** Claude writes more verbose code; `max_tokens=1800` cuts mid-expression. A configuration problem, not a capability problem. |
| GPT-4o | SyntaxError: EOF/unclosed (12); ValueError: wrong edge selection for fillet/chamfer (5); TypeError: unknown kwargs (2) | Mix of truncation and **API misuse** — hallucinates keyword arguments (`hole(offset=...)`) |
| Gemma-3-27B | TypeError: hallucinated methods (10); ValueError: null geometry (13) | **API hallucination** — invents non-existent methods (`workplane(center=...)`, `polygon(points=...)`, `.octagon()`, `.transform()`); also produces geometrically invalid chains ("Null TopoDS_Shape", "Cannot find solid") |
| Qwen2.5-VL-72B | 2 isolated failures | Near-perfect code generation |

**CAD sequence generation is the bottleneck, not drawing extraction.** All models produce roughly the right shape class (a bracket looks like a bracket), which means visual feature extraction from the drawing works. The failures come in translating that understanding into valid, dimensionally-correct CadQuery chains.

### Layer 2 — Shape quality failures (in the successful runs)

- **Dimensional inaccuracy**: median hausdorff 20–37 units across all models — models read the drawing qualitatively but don't extract precise dimensions from the annotations.
- **Complex/repeated geometry breaks xi_l2**: the worst outliers are consistently parts with repeating features — `ribs_plate` (Qwen xi_l2 = 14,123), `hose_clamp_stainless` (Gemma xi_l2 = 2,297). CadQuery operations like `.array()`, `.polarArray()`, and `.shell()` are rarely generated correctly.
- **Assembly-style parts fail silently**: multi-body geometries (`hose_clamp`, `crank_handle`) produce geometrically valid but wrong shapes — high hausdorff without a code error, because the model builds *a* shape but not the right one.
- **Simple primitives nearly solved**: `cube_with_beveled_corners`, `hexagonal_washer`, `standoff_spacer` all show low hausdorff and xi_l2, confirming models handle single-extrusion/chamfer shapes well.

**Summary of difficulty hierarchy** (easiest → hardest):
> single extrude/chamfer → revolve/shell → boolean combination → dimensionally-precise threading/holes → repeated/arrayed features → multi-body assemblies

---

## 3. Strategic Roadmap

The benchmark exposes two problems requiring different interventions. **Immediate fixes at the inference level** would dramatically change Claude's numbers (increase `max_tokens` to ≥4096 and add an explicit "output only executable Python, no markdown, no comments" instruction) and partially recover Gemma's API hallucinations via a system prompt with a canonical CadQuery cheatsheet and a few-shot example of correct step-by-step code. For the harder problem — dimensional accuracy and complex geometry — **supervised fine-tuning on (drawing image, ground-truth .py) pairs** is the critical next step: the model needs to learn to read tolerances and dimension annotations from the drawing, not just infer rough shape; this calls for chain-of-thought fine-tuning where the reasoning trace explicitly extracts each annotated dimension before writing a CadQuery line. Specific to repeated-feature failures, the fine-tuning dataset should oversample parts with `polarArray`, `shell`, and boolean operations, as these are the geometric classes where all models currently collapse. Starting from Qwen2.5-VL-72B as the base (highest code reliability) with LoRA fine-tuning on this dataset is the highest-leverage single action.
