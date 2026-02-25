# Part Metadata
# Part Number: 6253
# Part Name: split panel cover housing
# Version: 1
# Timestamp UTC: 20251218_033705
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular extrusion for the panel cover half
step0 = cq.Workplane("XY").box(120, 80, 5)
step1 = step0.faces(">Z").workplane().rect(100, 60).cutThruAll()
step2 = step1.faces(">Z").workplane().transformed(offset=(20, 30, 0)).circle(3).cutThruAll()
step3 = step2.faces(">Z").workplane().transformed(offset=(-40, 10, 0)).circle(1.5).cutThruAll()
step4 = step3.edges("|Z").fillet(2)
step5 = step4.edges("<Z or >Z").chamfer(0.5)
step6 = step5.faces("<X").workplane(centerOption="CenterOfMass").transformed(rotate=(0, 90, 0)).circle(5).extrude(4)
step7 = step6.faces(">Y").workplane().circle(1.8).cutThruAll()
result = step7