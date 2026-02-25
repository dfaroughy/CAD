# Part Metadata
# Part Number: 11978
# Part Name: square profile
# Version: 1
# Timestamp UTC: 20251218_033706
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base square profile extrusion
step0 = cq.Workplane("XY").box(50, 50, 5)

# Feature 1: Cut a central through hole along Z-axis
# Face selection, workplane, and sketch are part of this cut feature
step1 = step0.faces(">Z").workplane().circle(8).cutThruAll()

# Feature 2: Add four counterbore holes at corners, patterned in 2D
# Each hole is counterbored to allow bolt heads to sit flush
step2 = step1.faces(">Z").workplane() \
    .pushPoints([(15, 15), (15, -15), (-15, 15), (-15, -15)]) \
    .cskHole(6, 10, 90)

# Feature 3: Apply fillet to all vertical edges (edges parallel to Z)
step3 = step2.edges("|Z").fillet(3)

# Feature 4: Apply small fillet to top and bottom outer edges for deburring
step4 = step3.edges("<Z or >Z").fillet(1)

# Final result
result = step4