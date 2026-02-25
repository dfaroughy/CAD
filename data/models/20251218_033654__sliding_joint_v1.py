# Part Metadata
# Part Number: 1055
# Part Name: - sliding joint
# Version: 1
# Timestamp UTC: 20251218_033654
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create main body of sliding joint (base extrusion)
step0 = cq.Workplane("XY").box(60, 30, 15)
step1 = step0.faces(">Z").workplane().center(0, 0).rect(40, 10).cutThruAll()
step2 = step1.edges("|Z and <X").fillet(2)
step3 = step2.edges("|Z and >X").chamfer(1.5)
result = step3