# Part Metadata
# Part Number: 1045
# Part Name: - quick coupler
# Version: 1
# Timestamp UTC: 20251218_033657
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create main body of quick coupler (base extrusion)
step0 = cq.Workplane("XY").box(40, 30, 15)
step1 = step0.faces(">Y").workplane().circle(8).cutThruAll()
step2 = step1.faces(">Y").workplane().circle(10).extrude(10)
step3 = step2.edges("|Y").edges(">X").chamfer(1)
step4 = step2.faces(">Y").workplane().moveTo(8, 0).circle(2).revolve()
step5 = step4.edges("|Z").fillet(1.5)
step6 = step5.faces(">Y").workplane(offset=5).moveTo(10, 0).circle(1).revolve()
result = step6