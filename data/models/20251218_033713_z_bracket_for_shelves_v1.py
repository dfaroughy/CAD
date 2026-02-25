# Part Metadata
# Part Number: 9
# Part Name: z-bracket for shelves
# Version: 1
# Timestamp UTC: 20251218_033713
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: Yes

import cadquery as cq

# Feature 0: Create base vertical plate (extrusion)
step0 = cq.Workplane("XY").box(10, 50, 5)
step1 = step0.union(cq.Workplane("XZ").transformed(rotate=(90, 0, 0)).rect(10, 50).extrude(5))
step2 = step1.faces(">Y").workplane().circle(3).cutThruAll()
result = step2