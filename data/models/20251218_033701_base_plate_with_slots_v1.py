# Part Metadata
# Part Number: 8843
# Part Name: base plate with slots
# Version: 1
# Timestamp UTC: 20251218_033701
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular plate (extrusion)
step0 = cq.Workplane("XY").box(80, 60, 5)
step1 = step0.faces(">Z").workplane().center(-20, 0).slot2D(30, 10, 90).cutThruAll()
step2 = step1.faces(">Z").workplane().center(20, 0).slot2D(30, 10, 90).cutThruAll()
step3 = step2.edges("|Z").fillet(3)
step4 = step3.faces(">Z").workplane().center(-30, 20).cskHole(6, 10, 90)
result = step4