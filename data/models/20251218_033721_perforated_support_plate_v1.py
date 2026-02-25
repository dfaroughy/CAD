# Part Metadata
# Part Number: 8346
# Part Name: perforated support plate
# Version: 1
# Timestamp UTC: 20251218_033721
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular plate (extrusion)
step0 = cq.Workplane("XY").box(80, 60, 5)
step1 = step0.faces(">Z").workplane().circle(8).cutThruAll()
step2 = step1.faces(">Z").workplane().transformed(offset=(20, 20, 0)).circle(3.5).cutThruAll()
step3 = step2.faces(">Z").workplane().transformed(offset=(20, -20, 0)).circle(3.5).cutThruAll()
step4 = step3.faces(">Z").workplane().transformed(offset=(0, 15, 0)).circle(2).cutThruAll()
step5 = step4.faces(">Z").workplane().transformed(offset=(-15, 15, 0)).circle(2).cutThruAll()
step6 = step5.edges("|Z").fillet(1.5)
result = step6