# Part Metadata
# Part Number: 4
# Part Name: ceiling mount z-bracket
# Version: 1
# Timestamp UTC: 20251218_033713
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base plate of Z-bracket (first leg) - extruded rectangle
step0 = cq.Workplane("XY").box(50, 5, 10)
step1 = step0.faces(">Y").workplane(centerOption="CenterOfMass").transformed(rotate=(90, 0, 0))\
       .box(5, 50, 10, centered=(False, True, False))
step2 = step1.faces("<Z").workplane().center(-20, 0).circle(3).cutThruAll()
step3 = step2.faces("<Z").workplane().center(20, 0).circle(3).cutThruAll()
step4 = step3.edges("|Z").edges("<Y").edges(">X").fillet(2)
step5 = step4.edges(">Y").edges(">Z").chamfer(1)
step6 = step5.edges("|Z").edges(">Y").fillet(1)
result = step6