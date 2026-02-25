# Part Metadata
# Part Number: 5727
# Part Name: - box with gro
# Version: 1
# Timestamp UTC: 20251218_033700
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base box (extrusion)
step0 = cq.Workplane("XY").box(80, 60, 20)

# Feature 1: Create groove cutout along the top face (cut extrusion)
# Select top face, set workplane, draw rectangular groove profile, cut through height
step1 = step0.faces(">Z").workplane().rect(60, 10).cutBlind(-5)

# Feature 2: Add a central through hole from the top (cut extrusion)
step2 = step1.faces(">Z").workplane().circle(8).cutThruAll()

# Feature 3: Apply fillet to all vertical edges on the outer perimeter (edge fillet)
step3 = step2.edges("|Z and <X or |Z and <Y").fillet(3)

# Feature 4: Chamfer the top outer edges of the groove for easier insertion (chamfer)
step4 = step3.faces("<Z").edges("%Circle").chamfer(1)

# Final result
result = step4