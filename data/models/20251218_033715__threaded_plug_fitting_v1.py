# Part Metadata
# Part Number: 1562
# Part Name: - threaded plug fitting
# Version: 1
# Timestamp UTC: 20251218_033715
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 3
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create cylindrical base for plug (extrusion)
step0 = cq.Workplane("XY").circle(15).extrude(20)
step1 = step0.faces(">Z").workplane().circle(13).extrude(10)
step2 = step1.faces(">Z").workplane().polygon(6, 20).cutThruAll()
step3 = step2.faces(">Z").edges().chamfer(1)
step4 = step3.faces("<Z").edges().fillet(2)
result = step4