# Part Metadata
# Part Number: 1566
# Part Name: keyed coupling
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

# Feature 0: Create main cylindrical body (extrusion)
step0 = cq.Workplane("XY").circle(25).extrude(30)
step1 = step0.faces(">Z").workplane().circle(20).extrude(15)
step2 = step1.faces("<Z").workplane().circle(10).cutThruAll()
step3 = step2.faces("<Z").workplane(offset=-5).transformed(rotate=(0, 90, 0)) \
          .rect(6, 20, centered=(True, False)).cutBlind(-10)
step4 = step3.edges("|Z").edges("<Z").fillet(2)
step5 = step4.faces(">Z").edges().chamfer(1)
step6 = step5.faces("<Z").edges().fillet(0.5)
result = step6