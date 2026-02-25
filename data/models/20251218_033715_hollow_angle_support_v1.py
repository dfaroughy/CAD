# Part Metadata
# Part Number: 11447
# Part Name: hollow angle support
# Version: 1
# Timestamp UTC: 20251218_033715
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base L-angle profile extrusion (hollow section)
step0 = cq.Workplane("XY").polyline([(0, 0), (50, 0), (50, 5), (5, 5), (5, 50), (0, 50)]).close().extrude(30)
step1 = step0.faces(">Z").workplane(offset=0).polyline([(3, 3), (47, 3), (47, 5), (7, 5), (7, 47), (3, 47)]).close().cutThruAll()
step2 = step1.edges("#Z").edges(">X").edges(">Y").fillet(2)
step3 = step2.edges("#Z").edges("<X").edges("<Y").fillet(1)
result = step3