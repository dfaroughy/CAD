# Part Metadata
# Part Number: 5213
# Part Name: composite shapes
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

# Feature 0: Create main body with rectangular extrusion
step0 = cq.Workplane("XY").box(60, 40, 20)
step1 = step0.faces(">Z").workplane().moveTo(0, 0).circle(5).cutThruAll()
step2 = step1.faces(">Z").workplane(). \
    moveTo(20, 10).cboreHole(4, 8, 4). \
    moveTo(20, -10).cboreHole(4, 8, 4). \
    moveTo(-20, 10).cboreHole(4, 8, 4). \
    moveTo(-20, -10).cboreHole(4, 8, 4)
step3 = step2.edges("|Z").fillet(3)
step4 = step3.faces("<Z").edges("%Circle").chamfer(2)
result = step4