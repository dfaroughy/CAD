# Part Metadata
# Part Number: 7815
# Part Name: plastic lever mount
# Version: 1
# Timestamp UTC: 20251218_033657
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular extrusion for the lever mount body
step0 = cq.Workplane("XY").box(40, 60, 15)
step1 = step0.faces(">Z").workplane(offset=5).circle(6).cutThruAll()
step2 = step1.faces("<Z").workplane().pushPoints([(-15, -25), (15, -25), (-15, 25), (15, 25)]).circle(3).cutThruAll()
step3 = step2.edges("|Z").edges(">Z").fillet(3)
step4 = step2.edges("<Z").edges("%Circle").chamfer(1.5)
step5 = step4.faces(">Y").workplane(centerOption="CenterOfMass").transformed(rotate=(0, 90, 0)).box(8, 4, 6, combine=True)
result = step5