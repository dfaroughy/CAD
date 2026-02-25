# Part Metadata
# Part Number: 8853
# Part Name: gusseted circular mounting plate
# Version: 1
# Timestamp UTC: 20251218_033721
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: Yes

import cadquery as cq

# Feature 0: Create base circular plate (extrusion)
step0 = cq.Workplane("XY").circle(50).extrude(10)

# Feature 1: Cut central through hole (cut extrusion)
step1 = step0.faces(">Z").workplane().circle(10).cutThruAll()

# Feature 2: Add three evenly spaced mounting holes (cut pattern)
step2 = step1.faces(">Z").workplane().pushPoints([
    (35, 0),
    (-17.5, 30.31),
    (-17.5, -30.31)
]).circle(4).cutThruAll()

# Final result
result = step2