# Part Metadata
# Part Number: 11964
# Part Name: channel cross beam
# Version: 1
# Timestamp UTC: 20251218_033707
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular profile and extrude to form main beam body
step0 = cq.Workplane("XY").box(200, 60, 10)
step1 = step0.faces(">Z").workplane().rect(180, 40).cutThruAll()
step2 = step1.edges("|Z and >X").fillet(3)
step3 = step2.edges("<Z and |Y").chamfer(2)
result = step3