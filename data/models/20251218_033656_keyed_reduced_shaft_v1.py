# Part Metadata
# Part Number: 9371
# Part Name: keyed reduced shaft
# Version: 1
# Timestamp UTC: 20251218_033656
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create main cylindrical shaft body (extrusion)
step0 = cq.Workplane("XY").circle(10).extrude(50)
step1 = step0.faces(">Z").workplane(offset=-20).transformed(rotate=(0, 0, 90), offset=(0, 0, 0)) \
           .rect(4, 14, centered=(True, False)).extrude(-7, both=False)
step2 = step1.edges("|Z and <X").fillet(1)
step3 = step2.faces("<Z").workplane().circle(3).cutThruAll()
step4 = step3.faces("<Z").edges().chamfer(1)
step5 = step4.faces(">Z").edges("%Circle").chamfer(1)
result = step5