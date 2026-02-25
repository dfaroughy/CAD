# Part Metadata
# Part Number: 11961
# Part Name: angle iron frame
# Version: 1
# Timestamp UTC: 20251218_033709
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base L-section extrusion (angle iron profile)
step0 = cq.Workplane("XY").line(50, 0).line(0, 5).line(-45, 0).line(0, 45).line(-5, 0).line(0, -50).close().extrude(50)
step1 = step0.edges("|Z").fillet(2)
step2 = step1.edges("<Z").chamfer(1)
result = step2