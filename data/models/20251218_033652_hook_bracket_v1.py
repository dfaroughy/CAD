# Part Metadata
# Part Number: 521
# Part Name: hook bracket
# Version: 1
# Timestamp UTC: 20251218_033652
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular block for the bracket (extrusion)
step0 = cq.Workplane("XY").box(60, 40, 10)
step1 = step0.faces(">Y").workplane(centerOption="CenterOfMass").moveTo(0, 0).rect(8, 20).extrude(10)
step2 = step1.edges("|Z").edges("<X").fillet(5)
step3 = step2.edges(">X").edges("|Z").fillet(4)
step4 = step3.edges("|X").edges(">Z").chamfer(2)
result = step4