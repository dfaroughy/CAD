# Part Metadata
# Part Number: 8852
# Part Name: ribs plate
# Version: 1
# Timestamp UTC: 20251218_033725
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 2
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular plate (extrusion)
step0 = cq.Workplane("XY").box(120, 80, 15)
step1 = step0.faces(">Z").workplane().moveTo(-30, 0).circle(5).cutThruAll()
step2 = step1.faces(">Z").workplane().moveTo(30, 0).circle(5).cutThruAll()
step3 = step2.edges("|Z").fillet(3)
step4 = step3.faces(">Z").edges("%Circle").chamfer(2)
step5 = step4.faces(">Y").workplane(centerOption="CenterOfMass").transformed(offset=(0,0,7.5), rotate=(90,0,0))\
       .moveTo(-15, 0).lineTo(0, 10).lineTo(15, 0).lineTo(0, -10).close().extrude(10)
step6 = step5.mirror(mirrorPlane="XY")
result = step6