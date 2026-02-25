# Part Metadata
# Part Number: 17
# Part Name: thick-wall right angle bracket
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

# Feature 0: Create first arm of the right angle bracket (base extrusion)
step0 = cq.Workplane("XY").box(50, 10, 20)
step1 = step0.workplane(offset=0, origin=(0, 0, 0)).transformed(rotate=(0, 90, 0)).box(10, 50, 20, centered=(True, False, True))
step2 = step1.faces(">Y").workplane().moveTo(10, 0).circle(3).cutThruAll()
step3 = step2.faces(">Y").workplane().moveTo(-10, 0).circle(3).cutThruAll()
step4 = step3.edges("|Z").edges("<X").edges(">Y").fillet(5)
step5 = step4.edges("|Z").edges(">X").fillet(2)
step6 = step5.edges("|Z").edges(">Y").fillet(2)
result = step6