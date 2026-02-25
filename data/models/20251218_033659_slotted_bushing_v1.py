# Part Metadata
# Part Number: 7802
# Part Name: slotted bushing
# Version: 1
# Timestamp UTC: 20251218_033659
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create cylindrical base for bushing (extrusion)
step0 = cq.Workplane("XY").circle(15).extrude(20)

# Feature 1: Cut inner bore (through hole along Z-axis)
# Face selection and sketch are part of this cut feature
step1 = step0.faces(">Z").workplane().circle(10).cutThruAll()

# Feature 2: Create first slot from top face
# Select top face, create rectangular slot profile, cut through
step2 = step1.faces(">Z").workplane().transformed(offset=(0, 0, 0), rotate=(90, 0, 0)) \
        .rect(12, 2).cutThruAll()

# Feature 3: Create second slot perpendicular to first (90-degree rotation)
step3 = step2.faces(">Z").workplane().transformed(offset=(0, 0, 0), rotate=(90, 0, 90)) \
        .rect(12, 2).cutThruAll()

# Feature 4: Apply fillet to outer cylindrical edge for smooth finish
result = step3.edges("|Z").fillet(1)