# Part Metadata
# Part Number: 11450
# Part Name: channel girder
# Version: 1
# Timestamp UTC: 20251218_033714
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 2
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base channel profile (extrusion along Z)
step0 = cq.Workplane("XY").polyline([(0, 0), (60, 0), (60, 10), (10, 10), (10, 50), (0, 50)]).close().extrude(5)
step1 = step0.edges("<X and |Z").edges("%LINE").fillet(5)
step2 = step1.edges("|X and <Y").chamfer(2)
result = step2