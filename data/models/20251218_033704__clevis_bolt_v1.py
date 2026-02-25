# Part Metadata
# Part Number: 2093
# Part Name: - clevis bolt
# Version: 1
# Timestamp UTC: 20251218_033704
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create cylindrical shaft of the bolt (extrusion)
step0 = cq.Workplane("XY").circle(5).extrude(40)
step1 = step0.faces(">Z").workplane().polygon(6, 10).extrude(6)
step2 = step1.faces(">Y").workplane().transformed(offset=(0, 0, -20)).box(25, 15, 10, centered=(True, True, False))
step3 = step2.faces(">Z").workplane(offset=5).transformed(rotate=(90, 0, 0)).moveTo(0, 10).circle(4).cutThruAll().moveTo(0, -10).circle(4).cutThruAll()
step4 = step3.edges("|Z").edges("<Y").fillet(2)
step5 = step4.edges(">Z").chamfer(1)
step6 = step5.faces(">Z").workplane(offset=-6).circle(5).circle(4.2).extrude(-2)
result = step6