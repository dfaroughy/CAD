# Part Metadata
# Part Number: 5205
# Part Name: box with beveled corners
# Version: 1
# Timestamp UTC: 20251218_033705
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base box (extrusion)
step0 = cq.Workplane("XY").box(60, 40, 20)

# Feature 1: Apply beveled corners using chamfer on vertical edges
# Select all vertical edges and apply chamfer as a single feature operation
step1 = step0.edges("|Z").chamfer(5)

# Feature 2: Add a counterbored hole on the top face (cut feature)
# Workplane on top face, create counterbore hole through all
step2 = step1.faces(">Z").workplane().circle(3).cboreHole(6, 12, 8)

# Feature 3: Add a fillet to the top outer edge for aesthetic rounding
step3 = step2.faces(">Z").edges().fillet(1)

# Final result
result = step3