# Part Metadata
# Part Number: 530
# Part Name: wall mount bracket with tabs
# Version: 1
# Timestamp UTC: 20251218_033709
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create main bracket body (base extrusion)
step0 = cq.Workplane("XY").box(60, 40, 5)
step1 = step0.faces(">Y").workplane(centerOption="CenterOfMass").transformed(offset=(0, 0, 0), rotate=(0, 90, 0)).box(10, 5, 20)
step2 = step1.faces("<Y").workplane(centerOption="CenterOfMass").transformed(offset=(0, 0, 0), rotate=(0, 90, 0)).box(10, 5, 20)
step3 = step2.faces(">Z").workplane().circle(3.5).cutThruAll()
step4 = step3.faces(">Z").workplane(offset=0).move(0, 25).circle(3.5).cutThruAll()
step5 = step4.edges("|Z").fillet(2)
step6 = step5.edges("#Z").edges("<X").chamfer(1)
result = step6