# Part Metadata
# Part Number: 7821
# Part Name: - t-handle lever
# Version: 1
# Timestamp UTC: 20251218_033659
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create cylindrical handle base (extrusion)
step0 = cq.Workplane("XY").circle(15).extrude(80)
step1 = step0.faces(">Z").workplane().rect(20, 40).extrude(10)
step2 = step1.faces(">Z").edges().fillet(5)
step3 = step2.faces(">Z").workplane(centerOption="CenterOfMass").circle(6).cutThruAll()
step4 = step3.faces("<Z").edges().chamfer(2)
step5 = step4.faces(">Y").workplane(offset=5).moveTo(0, -10).circle(8).cutThruAll()
step6 = step5.edges("|X and >Y").fillet(3)
result = step6