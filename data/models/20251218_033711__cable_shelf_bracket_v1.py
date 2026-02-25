# Part Metadata
# Part Number: 8
# Part Name: - cable shelf bracket
# Version: 1
# Timestamp UTC: 20251218_033711
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular extrusion for the bracket
step0 = cq.Workplane("XY").box(40, 60, 5)
step1 = step0.faces(">Y").workplane(centerOption="CenterOfMass").move(0, 0).rect(10, 5).extrude(15)
step2 = step1.faces(">Z").workplane(centerOption="CenterOfMass").move(0, -15).rect(20, 8).cutThruAll()
step3 = step2.faces(">Z").workplane(centerOption="CenterOfMass").move(0, 30).circle(3.5).cutThruAll()
step4 = step3.faces(">X").workplane(centerOption="CenterOfMass").move(0, 5).circle(3).cutThruAll()
step5 = step4.edges("|Z and <Y").fillet(2)
step6 = step5.edges("|Z and >Y").chamfer(1)
step7 = step6.edges("|Z").edges(">X").fillet(1.5)
result = step7