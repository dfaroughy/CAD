# Benchmark Analysis

## Results Summary

| Model | Code Pass | Median vol_rel | Median hausdorff | Median $\xi_{L2}(r)$ | p_value > 0 |
|---|---|---|---|---|---|
| **Qwen2.5-VL-72B** | **98%** | 0.43 | 26.65 | 43.21 | 0 / 98 |
| **GPT-4o** | 77% | **0.30** | **20.07** | **33.33** | 1 / 77 |
| Gemma-3-27B | 63% | 0.57 | 30.06 | 60.54 | 0 / 63 |
| Claude-3.5-Sonnet | 7% | 0.65 | 24.52 | 62.82 | 0 / 7 |

**On p-values:** essentially all are 0 across all models. The p-value test is saturated, meaning every reconstructed shape is statistically distinguishable from ground truth. The only exception is one GPT-4o sample (`cube_with_beveled_corners`, to see other results go to `/Analysis/results/view_comparison`) which reaches p≈1 with hausdorff=0 and vol_rel=0 indicating a near-perfect reconstruction. The p-value is best treated as a "perfect match" detector rather than a graded similarity score. The continuous metrics (hausdorff, $\xi_{L2}(r)$) carry more information in the non-perfect regime.

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

### Code generation failures

| Model | Dominant error | Root cause |
|---|---|---|
| Claude-3.5-Sonnet | SyntaxError: *"unexpected EOF"*, *"'(' was never closed"* (77/92 failures) | **Truncation.** Claude writes more verbose code; `max_tokens=1800` cuts mid-expression. A configuration problem, not a capability problem. |
| GPT-4o | SyntaxError: EOF/unclosed (12); ValueError: wrong edge selection for fillet/chamfer (5); TypeError: unknown kwargs (2) | Mix of truncation and **API misuse** — hallucinates keyword arguments (`hole(offset=...)`) |
| Gemma-3-27B | TypeError: hallucinated methods (10); ValueError: null geometry (13) | **API hallucination** — invents non-existent methods (`workplane(center=...)`, `polygon(points=...)`, `.octagon()`, `.transform()`); also produces geometrically invalid chains ("Null TopoDS_Shape", "Cannot find solid") |
| Qwen2.5-VL-72B | 2 isolated failures | Near-perfect code generation |

**CAD sequence generation seems to be the main bottleneck, not drawing extraction.** All models produce roughly the right shape class (a bracket looks like a bracket), which means visual feature extraction from the drawing works. The failures come in translating that understanding into valid, dimensionally-correct CadQuery chains.

### Shape quality failure (in the successful runs)

- **Dimensional inaccuracy**: median hausdorff 20–37 units across all models implies the drawing qualitatively but don't extract precise dimensions from the annotations.

---

## 3. Strategic Roadmap

The benchmark exposes two problems requiring different interventions. 


 For the harder problem — dimensional accuracy and complex geometry — **supervised fine-tuning on (drawing image, ground-truth .py) pairs** is the critical next step: the model needs to learn to read tolerances and dimension annotations from the drawing, not just infer rough shape; this calls for chain-of-thought fine-tuning where the reasoning trace explicitly extracts each annotated dimension before writing a CadQuery line. Specific to repeated-feature failures, the fine-tuning dataset should oversample parts with `polarArray`, `shell`, and boolean operations, as these are the geometric classes where all models currently collapse. Starting from Qwen2.5-VL-72B as the base (highest code reliability) with LoRA fine-tuning on this dataset is the highest-leverage single action.
