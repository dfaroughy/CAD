# Part Metadata
# Part Number: 6775
# Part Name: split panel-mounted housing
# Version: 1
# Timestamp UTC: 20251218_033703
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create main outer body of the panel-mounted housing (base extrusion)
step0 = cq.Workplane("XY").box(80, 60, 25)
step1 = step0.faces(">Z").workplane(offset=0).rect(60, 40).cutThruAll()
step2 = step1.faces(">Y").workplane().moveTo(0, 0).rect(50, 20).cutThruAll()
step3 = step2.edges("|Z and >X").fillet(2)
step4 = step3.edges("|Z and <X").fillet(2)
step5 = step4.edges("|X and <Z").chamfer(1)
result = step5