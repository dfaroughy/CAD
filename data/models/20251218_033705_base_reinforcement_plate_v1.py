# Part Metadata
# Part Number: 8328
# Part Name: base reinforcement plate
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

# Feature 0: Create base rectangular plate (extrusion)
step0 = cq.Workplane("XY").box(120, 80, 8)

# Feature 1: Add four counterbored holes near corners (cut extrusion with workplane and circle chain)
step1 = step0.faces(">Z").workplane().pushPoints([(-50, -30), (50, -30), (-50, 30), (50, 30)]).circle(6).cboreHole(12, 4, 8)

# Feature 2: Add central through hole (cut extrusion)
step2 = step1.faces(">Z").workplane().circle(10).cutThruAll()

# Feature 3: Add fillet to all vertical edges of the base plate
step3 = step2.edges("|Z").fillet(3)

# Feature 4: Add chamfer to top and bottom perimeter edges (non-vertical edges)
step4 = step3.edges("<Z or >Z").edges("%CIRCLE").chamfer(1.5)

# Final result
result = step4