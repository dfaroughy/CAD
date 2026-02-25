# Part Metadata
# Part Number: 13
# Part Name: - cable t-bracket
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

# Feature 0: Create main vertical base plate (extrusion)
step0 = cq.Workplane("XY").box(20, 5, 40)
step1 = step0.faces(">Z").workplane(centerOption="CenterOfMass").transformed(rotate=(90, 0, 0)).box(30, 5, 5)
step2 = step1.faces(">Y").workplane().center(0, 0).rect(8, 20).cutThruAll()
step3 = step2.edges("|Y").edges("<Z").fillet(2)
step4 = step3.edges("#X").edges("<X").fillet(1.5)
step5 = step4.edges("|Z").edges(">Y").chamfer(1)
result = step5