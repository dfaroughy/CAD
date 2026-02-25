# Part Metadata
# Part Number: 8851
# Part Name: rubber plate
# Version: 1
# Timestamp UTC: 20251218_033659
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular extrusion for rubber plate
step0 = cq.Workplane("XY").box(120, 80, 5)
step1 = step0.faces(">Z").workplane().center(30, 20).circle(6).cutThruAll()
step2 = step1.faces(">Z").workplane().center(-30, 20).circle(6).cutThruAll()
step3 = step2.faces(">Z").workplane().center(-30, -20).circle(6).cutThruAll()
step4 = step3.edges("|Z").fillet(3)
step5 = step4.edges("<Z or >Z").chamfer(1.5)
result = step5