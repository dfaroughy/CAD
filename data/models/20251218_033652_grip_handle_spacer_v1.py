# Part Metadata
# Part Number: 7294
# Part Name: grip handle spacer
# Version: 1
# Timestamp UTC: 20251218_033652
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular extrusion for the spacer body
step0 = cq.Workplane("XY").box(40, 20, 8)
step1 = step0.faces(">Z").workplane().circle(6).cutThruAll()
step2 = step1.faces(">Z").workplane().center(-10, 0).cboreHole(3, 6, 3)
step3 = step2.edges("|Z").fillet(1.5)
step4 = step3.edges("#Z").chamfer(0.5)
result = step4