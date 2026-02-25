import re

import cadquery as cq
import numpy as np
from scipy.spatial import KDTree
from scipy.stats import chi2 as chi2_dist

from utils import _extract_cad_model, shape_to_pointcloud, shape_to_uniform_pointcloud


def results(obj1: cq.Workplane, obj2: cq.Workplane):
    dV = shape_volume_dist(obj1, obj2)['rel_diff']
    haus = point_cloud_dist(obj1, obj2)['hausdorff']
    xi_L2 = two_point_corr_dist(obj1, obj2, n_bins=64)['l2']
    pv = combined_pvalue(obj1, obj2, n_bins=20)

    print(f"Volume Relative Difference:  {dV:.4f}")
    print(f"Hausdorff Distance:          {haus:.4f}")
    print(f"xi(r) Landy-Szalay L2:       {xi_L2:.4f}")
    print(f"p-value (Fisher):            {pv['p_value']:.4f}  "
          f"[z_hausdorff={pv['z_scores']['hausdorff']:.2f}, "
          f"z_chamfer={pv['z_scores']['chamfer']:.2f}]")
    return {"vol_rel": dV, "hausdorff": haus, "xi_l2": xi_L2, "p_value": pv['p_value']}


#...triangulation-based metrics

def shape_surface_area(obj: cq.Workplane, tol=0.05):
    vertices, triangles = obj.val().tessellate(tol)
    pts = np.array([[v.x, v.y, v.z] for v in vertices])
    tris = np.array(triangles)
    v0, v1, v2 = pts[tris[:, 0]], pts[tris[:, 1]], pts[tris[:, 2]]
    areas = np.linalg.norm(np.cross(v1 - v0, v2 - v0), axis=1) / 2
    return float(areas.sum())


def shape_surface_area_dist(obj1: cq.Workplane, obj2: cq.Workplane, tol=0.05):
    a1 = shape_surface_area(obj1, tol=tol)
    a2 = shape_surface_area(obj2, tol=tol)
    return {
        "area1":    a1,
        "area2":    a2,
        "abs_diff": abs(a1 - a2),
        "rel_diff": abs(a1 - a2) / a1 if a1 > 0 else float("inf"),
    }


def shape_volume_dist(obj1: cq.Workplane, obj2: cq.Workplane):
    v1 = float(obj1.val().Volume())
    v2 = float(obj2.val().Volume())
    return {
        "vol1":     v1,
        "vol2":     v2,
        "abs_diff": abs(v1 - v2),
        "rel_diff": abs(v1 - v2) / v1 if v1 > 0 else float("inf"),
    }



#...pointcloud-based metrics

def point_cloud_dist(obj1: cq.Workplane, obj2: cq.Workplane, n_points: int=1000, tol: float=0.05, uniform: str=False):

    if uniform:
        pts1 = shape_to_uniform_pointcloud(obj1, n_points=n_points, tol=tol)
        pts2 = shape_to_uniform_pointcloud(obj2, n_points=n_points, tol=tol)
    else:
        pts1 = shape_to_pointcloud(obj1, tol=tol)
        pts2 = shape_to_pointcloud(obj2, tol=tol)

    d1 = KDTree(pts2).query(pts1)[0]
    d2 = KDTree(pts1).query(pts2)[0]

    all_d = np.concatenate([d1, d2])
    return {
        "hausdorff": max(d1.max(), d2.max()),
        "chamfer":   np.mean(d1 ** 2) + np.mean(d2 ** 2),
    }


def point_cloud_dist_stats(obj1: cq.Workplane, obj2: cq.Workplane, tol: float=0.05):
    def _runs(a, b):
        results = [point_cloud_dist(a, b, tol=tol)
                   for _ in range(1)]
        return {m: np.array([r[m] for r in results]) for m in ["hausdorff", "chamfer"]}

    signal = _runs(obj1, obj2)
    noise1 = _runs(obj1, obj1)
    noise2 = _runs(obj2, obj2)

    out = {}
    for m in ["hausdorff", "chamfer"]:
        s_mean, s_std = signal[m].mean(), signal[m].std()
        n1_mean, n1_std = noise1[m].mean(), noise1[m].std()
        n2_mean, n2_std = noise2[m].mean(), noise2[m].std()

        noise_baseline = (n1_mean + n2_mean) / 2
        noise_baseline_std = np.sqrt(n1_std**2 + n2_std**2) / 2

        corrected = s_mean - noise_baseline
        z = corrected / np.sqrt(s_std**2 + noise_baseline_std**2 + 1e-12)

        out[m] = {
            "corrected":    corrected,
            "z_score":      z,
            "signal_mean":  s_mean,
            "signal_std":   s_std,
            "noise1_mean":  n1_mean,
            "noise2_mean":  n2_mean,
        }
    return out

#...2-point correlator-based metrics: SO(3)-invariant but more expensive

def _paircount(pts, n_bins=20, n_sub=10_000):
    """Histogram of pairwise distances — the surface equivalent of the 2PCF."""
    rng = np.random.default_rng(0)
    idx = rng.choice(len(pts), min(n_sub, len(pts)), replace=False)
    sub = pts[idx]
    # sample random pairs to avoid O(N²) — approximate but fast
    i = rng.integers(0, len(sub), size=100_000)
    j = rng.integers(0, len(sub), size=100_000)
    mask = i != j
    dists = np.linalg.norm(sub[i[mask]] - sub[j[mask]], axis=1)
    r_max = np.percentile(dists, 99)
    counts, edges = np.histogram(dists, bins=n_bins, range=(0, r_max), density=True)
    centers = (edges[:-1] + edges[1:]) / 2
    return centers, counts


def piont_cloud_paircount_dist(obj1: cq.Workplane, obj2: cq.Workplane, n_points: int=1000, n_bins: int=20, tol: float=0.05, uniform: str=False):
    """L2 distance between the paircount histograms of two shapes."""
    
    if uniform:
        pts1 = shape_to_uniform_pointcloud(obj1, n_points=n_points, tol=tol)
        pts2 = shape_to_uniform_pointcloud(obj2, n_points=n_points, tol=tol)
    else:
        pts1 = shape_to_pointcloud(obj1, n_points=n_points, tol=tol)
        pts2 = shape_to_pointcloud(obj2, n_points=n_points, tol=tol)

    r1, c1 = _paircount(pts1, n_bins=n_bins)
    r2, c2 = _paircount(pts2, n_bins=n_bins)
    return float(np.sqrt(np.sum((c1 - c2) ** 2)))  # L2 on histogram


def two_point_corr_Landy_Szalay(obj1, obj2, tol=0.05, n_bins=20):
    """
    Landy-Szalay 2-point correlation function between two CAD shapes.

    obj1 = reference (R), obj2 = data (D).
    KDTree.count_neighbors gives cumulative pair counts at each bin edge,
    so no external package is needed.

    ξ(r) = (DD/norm_DD - 2*DR/norm_DR + RR/norm_RR) / (RR/norm_RR)

    ξ(r) ≈ 0 at all scales when shapes are identical.
    ξ(r) > 0: obj2 has more pairs than obj1 at scale r.
    ξ(r) < 0: obj2 has fewer pairs than obj1 at scale r.
    """
    pts_R = shape_to_pointcloud(obj1, tol=tol).astype(np.float64)
    pts_D = shape_to_pointcloud(obj2, tol=tol).astype(np.float64)

    N_D, N_R = len(pts_D), len(pts_R)

    all_pts = np.concatenate([pts_R, pts_D])
    R_max = float(np.linalg.norm(all_pts - all_pts.mean(axis=0), axis=1).max())
    bin_edges = np.logspace(np.log10(R_max * 1e-2), np.log10(R_max * 2.0), n_bins + 1)
    r_centers = np.sqrt(bin_edges[:-1] * bin_edges[1:])  # geometric bin centers

    tree_D = KDTree(pts_D)
    tree_R = KDTree(pts_R)

    # Cumulative pair counts at each bin edge
    DD_cum = tree_D.count_neighbors(tree_D, bin_edges)
    RR_cum = tree_R.count_neighbors(tree_R, bin_edges)
    DR_cum = tree_D.count_neighbors(tree_R, bin_edges)

    # Pairs per bin; auto-counts include (i,j) and (j,i) so divide by 2
    DD = np.diff(DD_cum) / 2.0
    RR = np.diff(RR_cum) / 2.0
    DR = np.diff(DR_cum)

    norm_DD = N_D * (N_D - 1) / 2.0
    norm_RR = N_R * (N_R - 1) / 2.0
    norm_DR = float(N_D * N_R)

    with np.errstate(invalid="ignore", divide="ignore"):
        xi = np.where(
            RR > 0,
            (DD / norm_DD - 2.0 * DR / norm_DR + RR / norm_RR) / (RR / norm_RR),
            0.0,
        )

    # Poisson variance: σ²(r) ≈ (1 + ξ)² / RR
    varxi = np.where(RR > 0, (1.0 + xi) ** 2 / RR, 0.0)

    return r_centers, xi, varxi


def two_point_corr_dist(obj1, obj2, n_points=10_000, tol=0.05, n_bins=20):
    """
    Scalar distance derived from the LS 2PCF.

    chi2 = Σ ξ(r)² / σ²(r)  — bins where shapes differ contribute most.
    l2   = sqrt(Σ ξ(r)²)     — unweighted summary.
    """
    r, xi, varxi = two_point_corr_Landy_Szalay(obj1, obj2, tol=tol, n_bins=n_bins)
    chi2 = float(np.sum(xi ** 2 / (varxi + 1e-12)))
    l2   = float(np.sqrt(np.sum(xi ** 2)))
    return {"r": r, "xi": xi, "varxi": varxi, "chi2": chi2, "l2": l2}


def combined_pvalue(obj1, obj2, n_points: int = 1000, n_runs: int = 5,
                 tol: float = 0.05, uniform: bool = False, n_bins: int = 20):
    """
    Combined p-value via Fisher's method over two independent sub-tests:

      1. Point-cloud test  — chi2(2) from Hausdorff + Chamfer noise-corrected z-scores.
      2. 2PCF test         — chi2(n_bins) from the Landy-Szalay xi(r) statistic.

    Fisher's combined statistic: F = -2*(log(p_pc) + log(p_xi)) ~ chi2(4).

    H0: obj1 and obj2 are the same shape.  Small p-value -> shapes are distinct.
    """
    # --- point-cloud z-scores -> chi2(2) ---
    pc_stats = point_cloud_dist_stats(obj1, obj2, tol=tol)
    z_scores = np.array([pc_stats[m]["z_score"] for m in ["hausdorff", "chamfer"]])
    chi2_pc  = float(np.sum(z_scores ** 2))
    p_pc     = float(1 - chi2_dist.cdf(chi2_pc, df=2))

    # --- LS 2PCF chi2(n_bins) ---
    xi_res   = two_point_corr_dist(obj1, obj2, tol=tol, n_bins=n_bins)
    chi2_xi  = xi_res["chi2"]
    p_xi     = float(1 - chi2_dist.cdf(chi2_xi, df=n_bins))

    # --- Fisher's method: -2 * sum(log(p_i)) ~ chi2(2k), k=2 tests ---
    p_pc_safe  = max(p_pc, 1e-300)
    p_xi_safe  = max(p_xi, 1e-300)
    fisher     = float(-2.0 * (np.log(p_pc_safe) + np.log(p_xi_safe)))
    p_combined = float(1 - chi2_dist.cdf(fisher, df=4))

    return {
        "p_value":     p_combined,
        "fisher_stat": fisher,
        "p_pc":        p_pc,
        "p_xi":        p_xi,
        "chi2_pc":     chi2_pc,
        "chi2_xi":     chi2_xi,
        "z_scores":    {m: float(pc_stats[m]["z_score"]) for m in ["hausdorff", "chamfer"]},
    }


# --- code-level metrics ---

def code_runs(filepath: str):
    """
    Execute a CadQuery.py file line-by-line and report success or the first failure.

    Returns:
        success      bool        True if the entire file ran without exception.
        n_steps_ok   int         Number of step* variables successfully assigned.
        has_result   bool        True if 'result' was successfully assigned.
        error_step   str|None    Variable name being assigned when the error occurred.
        error_type   str|None    Exception class name (e.g. 'ValueError').
        error_msg    str|None    First line of the exception message.
    """
    try:
        code = _extract_cad_model(filepath)
    except Exception as e:
        return {
            "success":    False,
            "n_steps_ok": 0,
            "has_result": False,
            "error_step": None,
            "error_type": type(e).__name__,
            "error_msg":  str(e).splitlines()[0],
        }

    namespace  = {"cq": cq}
    n_steps_ok = 0
    has_result = False
    last_step  = None
    steps_ok   = []

    for line in code.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            exec(line, namespace)
            m = re.match(r"^(step\d+)\s*=", line)
            if m:
                last_step = m.group(1)
                n_steps_ok += 1
                steps_ok.append(m.group(1))
            if re.match(r"^result\s*=", line) and "result" in namespace:
                has_result = True
        except Exception as e:
            m = re.match(r"^(step\d+|result)\s*=", line)
            return {
                "success":    False,
                "n_steps_ok": n_steps_ok,
                "has_result": has_result,
                "steps_ok":   steps_ok,
                "error_step": m.group(1) if m else last_step,
                "error_type": type(e).__name__,
                "error_msg":  str(e).splitlines()[0],
            }

    return {
        "success":    True,
        "n_steps_ok": n_steps_ok,
        "has_result": has_result,
        "steps_ok":   steps_ok,
        "error_step": None,
        "error_type": None,
        "error_msg":  None,
    }


def code_pass_rate(directory: str):
    """
    Run code_runs on every .py file in a directory and return aggregate stats.

    Returns:
        pass_rate   float                  Fraction of files that ran without error.
        n_total     int                    Total .py files found.
        n_passed    int                    Files with success=True.
        n_failed    int                    Files with success=False.
        per_step    dict[str, float]       Pass rate per step key: {'step0': 0.9, ..., 'result': 0.7}.
        results     dict[str, dict]        Per-file code_runs output, keyed by filename.
    """
    from pathlib import Path

    files = sorted(Path(directory).glob("*.py"))
    results = {f.name: code_runs(str(f)) for f in files}

    n_total  = len(results)
    n_passed = sum(1 for r in results.values() if r["success"])
    n_failed = n_total - n_passed

    # collect all step names seen across files, sort numerically
    all_steps = sorted(
        {s for r in results.values() for s in r.get("steps_ok", [])},
        key=lambda s: int(re.search(r"\d+", s).group()),
    )
    per_step = {
        step: sum(1 for r in results.values() if step in r.get("steps_ok", [])) / n_total
        for step in all_steps
    }
    per_step["result"] = (
        sum(1 for r in results.values() if r["has_result"]) / n_total
        if n_total > 0 else float("nan")
    )

    return {
        "pass_rate": n_passed / n_total if n_total > 0 else float("nan"),
        "n_total":   n_total,
        "n_passed":  n_passed,
        "n_failed":  n_failed,
        "per_step":  per_step,
        "results":   results,
    }


def code_error_bins(directory: str):
    """
    Bin CadQuery execution results by exception type across all .py files in a directory.

    Returns a dict keyed by error type ('passed', 'Standard_Failure', 'ValueError',
    'SyntaxError', ...), sorted with 'passed' first then by frequency. Each value is:
        count     int    Number of files in this bin.
        fraction  float  Fraction of total files.
        files     list   Filenames belonging to this bin.
    """
    rate    = code_pass_rate(directory)
    results = rate["results"]
    n_total = rate["n_total"]

    bins = {}
    for fname, r in results.items():
        key = "passed" if r["success"] else (r.get("error_type") or "unknown")
        if key not in bins:
            bins[key] = {"count": 0, "fraction": 0.0, "files": []}
        bins[key]["count"] += 1
        bins[key]["files"].append(fname)

    for v in bins.values():
        v["fraction"] = v["count"] / n_total if n_total > 0 else float("nan")

    # passed first, then by count descending
    return dict(
        sorted(bins.items(), key=lambda kv: (kv[0] != "passed", -kv[1]["count"]))
    )
