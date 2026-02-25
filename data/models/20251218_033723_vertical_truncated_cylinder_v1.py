# Part Metadata
# Part Number: 5227
# Part Name: vertical truncated cylinder
# Version: 1
# Timestamp UTC: 20251218_033723
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create vertical truncated cylinder base (cylinder extrusion)
step0 = cq.Workplane("XY").circle(25).extrude(50)

# Feature 1: Truncate the top with a diagonal cut (cut plane at angle)
# Using a box to boolean cut the top at a slant
step1 = step0.faces(">Z").workplane(offset=0).transformed(rotate=(15, 0, 0)).box(60, 60, 60, centered=(True, True, False), combine=False)
result = step0.cut(step1)