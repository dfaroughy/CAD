# Part Metadata
# Part Number: 5218
# Part Name: cube with beveled corners
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

# Feature 0: Create base cube (extrusion)
step0 = cq.Workplane("XY").box(50, 50, 50)

# Feature 1: Apply bevel (chamfer) to all vertical edges
step1 = step0.edges().chamfer(5)

# Final result
result = step1