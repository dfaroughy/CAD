# Part Metadata
# Part Number: 5206
# Part Name: box with fillet
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

# Feature 0: Create base rectangular box (extrusion)
step0 = cq.Workplane("XY").box(60, 40, 20)

# Feature 1: Apply fillet to all vertical edges (edge rounding)
result = step0.edges("|Z").fillet(5)