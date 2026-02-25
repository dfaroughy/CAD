# Part Metadata
# Part Number: 3125
# Part Name: cryo-thermal shock restraint mount
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

# Feature 0: Create base rectangular block for the mount (extrusion)
step0 = cq.Workplane("XY").box(60, 40, 15)
step1 = step0.faces(">Z").workplane().rect(30, 8).cutBlind(-5)
step2 = step1.faces(">Z").workplane().pushPoints([(-20, 0), (20, 0)]).circle(3.5).cutThruAll()
step3 = step2.faces("<Y").workplane(centerOption="CenterOfMass").moveTo(0, 0).circle(2.5).cutThruAll()
step4 = step3.edges("|Z").fillet(2)
step5 = step4.edges("<X or >X or <Y or >Y").chamfer(1)
step6 = step5.faces("<Z").workplane().moveTo(0, -10).circle(2.5).cutBlind(6)
result = step6