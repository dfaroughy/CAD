# Part Metadata
# Part Number: 11967
# Part Name: reinforced profile
# Version: 1
# Timestamp UTC: 20251218_033717
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create main profile base extrusion (rectangular cross-section)
step0 = cq.Workplane("XY").rect(60, 40).extrude(100)
step1 = step0.faces(">Y").workplane(centerOption="CenterOfMass").circle(8).cutThruAll()
step2 = step1.faces(">X").workplane(centerOption="CenterOfMass").transformed(offset=(0,0,0), rotate=(0,90,0)).rect(20, 15).cutThruAll()
step3 = step2.edges("|Z").fillet(3)
step4 = step3.edges(">Z").edges("|X").chamfer(1.5)
step5 = step4.faces("<Z").workplane().pushPoints([(-20, -15), (20, -15)]).circle(2.5).cutThruAll()
result = step5