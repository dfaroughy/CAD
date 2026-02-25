# Part Metadata
# Part Number: 5744
# Part Name: - cube with ridge
# Version: 1
# Timestamp UTC: 20251218_033709
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
step0 = cq.Workplane("XY").box(50, 50, 10)

# Feature 1: Add ridge along the centerline on top face (extrusion)
# Select top face, create workplane, draw rectangle for ridge profile, extrude upward
step1 = step0.faces(">Z").workplane().rect(50, 5).extrude(5)

# Feature 2: Apply fillet to the ridge top edges for smooth finish
# Select edges along the top of the ridge (lengthwise), apply small fillet
step2 = step1.edges("|Z and <X and >Y").fillet(1)

# Feature 3: Apply chamfer to four bottom corners of the base cube
# Select vertical edges of base, apply chamfer
step3 = step2.edges("|Z").edges("<X or >X or <Y or >Y").chamfer(2)

# Final result
result = step3