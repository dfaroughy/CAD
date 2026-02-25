# Part Metadata
# Part Number: 5739
# Part Name: pyramid with rounded base
# Version: 1
# Timestamp UTC: 20251218_033655
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create a pyramid base using a square and extrude with taper
step0 = cq.Workplane("XY").rect(40, 40).workplane(offset=20).rect(0.1, 0.1).loft(combine=True)

# Feature 1: Apply a fillet to the bottom edges of the pyramid base to round the base part
# Select only the bottom outer edges (at Z=0) and apply fillet
result = step0.edges("<Z").fillet(3)