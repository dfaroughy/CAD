# Part Metadata
# Part Number: 5731
# Part Name: hollow torus
# Version: 1
# Timestamp UTC: 20251218_033701
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create hollow torus by revolving a circle around the Z-axis (revolve operation)
step0 = cq.Workplane("XZ").moveTo(50, 0).circle(10).revolve()
result = step0