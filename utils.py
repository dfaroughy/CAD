
import numpy as np
import cadquery as cq
import ast
import re
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def _extract_cad_model(filepath: str, output: str=None):
    with open(filepath, "r") as f:
        lines = f.readlines()
    code_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("import ") or stripped.startswith("from "):
            continue
        code_lines.append(line.rstrip())
    code_string = "\n".join(code_lines)
    if output == 'workplane':
        namespace = {"cq": cq}
        try:
            exec(code_string, namespace)
        except Exception:
            return None
        return namespace.get("result", None)
    return code_string


def cad_model_seq(filepath: str) -> dict:
    code = _extract_cad_model(filepath)
    namespace = {"cq": cq}
    steps = {}
    for line in code.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            exec(line, namespace)
        except Exception:
            steps["result"] = None
            return steps
        match = re.match(r"^(step\d+)\s*=", line)
        if match:
            steps[match.group(1)] = namespace[match.group(1)]
    steps["result"] = namespace.get("result", None)
    return steps

def shape_to_pointcloud(obj: cq.Workplane, tol=0.05):
    vertices, _ = obj.val().tessellate(tol)
    return np.array([[v.x, v.y, v.z] for v in vertices])
    
    
def shape_to_uniform_pointcloud(obj: cq.Workplane, n_points=5000, tol=0.05):
    vertices, triangles = obj.val().tessellate(tol)
    pts = np.array([[v.x, v.y, v.z] for v in vertices])
    tris = np.array(triangles)

    # Triangle areas for weighted sampling
    v0, v1, v2 = pts[tris[:, 0]], pts[tris[:, 1]], pts[tris[:, 2]]
    areas = np.linalg.norm(np.cross(v1 - v0, v2 - v0), axis=1) / 2
    probs = areas / areas.sum()

    # Sample triangles, then random barycentric coords within each
    chosen = np.random.choice(len(tris), size=n_points, p=probs)
    r1, r2 = np.random.rand(n_points, 1), np.random.rand(n_points, 1)
    mask = r1 + r2 > 1
    r1[mask], r2[mask] = 1 - r1[mask], 1 - r2[mask]
    return v0[chosen] + r1 * (v1[chosen] - v0[chosen]) + r2 * (v2[chosen] - v0[chosen])



# plotting utilities


def show_3d(obj, figsize=(5, 5), color=None, alpha=0.1):

    vertices, triangles = obj.val().tessellate(0.01)
    verts = [[[vertices[i].x, vertices[i].y, vertices[i].z] for i in tri] for tri in triangles]

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection="3d")
    poly = Poly3DCollection(verts, alpha=alpha, linewidth=0.2, edgecolor="k")
    poly.set_facecolor(color)
    ax.add_collection3d(poly)
    pts = np.array([[v.x, v.y, v.z] for v in vertices])
    ax.set_xlim(pts[:, 0].min(), pts[:, 0].max())
    ax.set_ylim(pts[:, 1].min(), pts[:, 1].max())
    ax.set_zlim(pts[:, 2].min(), pts[:, 2].max())
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()

def show_3d_point_cloud(points, figsize=(5, 5), color="steelblue", alpha=0.8, s=.1, marker=','):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=s, marker=marker, color=color, alpha=alpha)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.tight_layout()
    plt.show()