# Part Metadata
# Part Number: 2621
# Part Name: cap nut with spring
# Version: 1
# Timestamp UTC: 20251218_033718
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 2
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create cylindrical base of cap nut (extrusion)
step0 = cq.Workplane("XY").circle(6).extrude(8)
step1 = step0.faces(">Z").workplane(centerOption="CenterOfMass").polygon(6, 12).extrude(4)
step2 = step1.faces(">Z").workplane(centerOption="CenterOfMass").circle(3).cutThruAll()
step3 = step2.faces(">Z").workplane(centerOption="CenterOfMass").circle(4.5).extrude(-2)
step4 = step3.faces(">Z").edges().chamfer(0.5)
step5 = step4.faces("<Z").edges().fillet(0.5)
result = step5