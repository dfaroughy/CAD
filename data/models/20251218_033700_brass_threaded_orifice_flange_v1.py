# Part Metadata
# Part Number: 3654
# Part Name: brass threaded orifice flange
# Version: 1
# Timestamp UTC: 20251218_033700
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create main cylindrical body (extrusion)
step0 = cq.Workplane("XY").circle(30).extrude(15)
step1 = step0.faces(">Z").workplane().circle(50).extrude(5)
step2 = step1.faces(">Z").workplane().circle(10).cutThruAll()
step3 = step2.faces(">Z").workplane().circle(3.5).circle(50).extrude(-7)
step4 = step3.faces("<Z").workplane(offset=2).circle(28).extrude(-2)
step5 = step4.edges(cq.selectors.NearestToPointSelector((0, 0, 15))).chamfer(1)
step6 = step5.edges(cq.selectors.NearestToPointSelector((0, 0, 15))).fillet(2)
step7 = step6.faces(">Z").edges(cq.selectors.NearestToPointSelector((50, 0, 20))).chamfer(1.5)
result = step7