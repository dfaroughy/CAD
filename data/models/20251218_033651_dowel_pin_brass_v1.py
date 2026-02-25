# Part Metadata
# Part Number: 2616
# Part Name: dowel pin brass
# Version: 1
# Timestamp UTC: 20251218_033651
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create cylindrical base for dowel pin (extrusion)
step0 = cq.Workplane("XY").circle(3.0).extrude(20.0)
step1 = step0.edges(">Z").fillet(0.5)
step2 = step1.edges("<Z").chamfer(0.3)
result = step2