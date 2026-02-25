# Part Metadata
# Part Number: 534
# Part Name: bracket fitting
# Version: 1
# Timestamp UTC: 20251218_033658
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create main bracket base (extrusion)
step0 = cq.Workplane("XY").box(60, 40, 15)
step1 = step0.faces(">Y").workplane(centerOption="CenterOfMass").transformed(offset=(0, 0, 20)).box(8, 60, 5, combine=True)
step2 = step1.faces(">Z").workplane().moveTo(0, 0).rect(30, 8).cutThruAll()
step3 = step2.edges("|Z and >X and >Y").fillet(4)
step4 = step3.edges("|Z and >X and <Y").chamfer(3)
step5 = step4.edges("|Y and <Z").fillet(2)
result = step5