# Part Metadata
# Part Number: 10404
# Part Name: wedge cam linkage pivot
# Version: 1
# Timestamp UTC: 20251218_033719
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 3
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base wedge cam profile via extrusion
step0 = cq.Workplane("XY").polyline([(0, 0), (30, 0), (20, 10), (0, 10)]).close().extrude(8)
step1 = step0.faces(">Z").workplane().moveTo(15, 5).circle(3).cutThruAll()
step2 = step1.faces(">Y").workplane(centerOption="CenterOfMass").moveTo(-10, 0).rect(12, 6).cutThruAll()
step3 = step2.edges("|Z").fillet(1.0)
step4 = step3.faces(">Z").edges().chamfer(0.8)
step5 = step4.faces("<Z").edges("%Circle").chamfer(0.5)
result = step5