# Part Metadata
# Part Number: 5730
# Part Name: tilted square pyramid
# Version: 1
# Timestamp UTC: 20251218_033719
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: Yes

import cadquery as cq

# Feature 0: Create base square of the pyramid (a flat plate)
step0 = cq.Workplane("XY").box(50, 50, 2)
step1 = step0.faces(">Z").workplane().transformed(offset=(10, 10, 0)).rect(10, 10).extrude(25, taper=2)
result = step1