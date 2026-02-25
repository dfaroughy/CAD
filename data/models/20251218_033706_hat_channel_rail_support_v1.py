# Part Metadata
# Part Number: 11973
# Part Name: hat channel rail support
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

# Feature 0: Create base extrusion for hat channel rail support (main body)
step0 = cq.Workplane("XY").box(80, 40, 5)

# Feature 1: Extrude central hat channel profile upward from top face
step1 = step0.faces(">Z").workplane() \
    .rect(70, 30) \
    .workplane(offset=2.5) \
    .rect(60, 20) \
    .loft(combine=True)

# Feature 2: Cut mounting hole in center of base (through all)
step2 = step1.faces("<Z").workplane() \
    .circle(4) \
    .cutThruAll()

# Feature 3: Cut two side clearance holes for rail attachment
step3 = step2.faces("<Z").workplane() \
    .pushPoints([(-25, 0), (25, 0)]) \
    .circle(3.5) \
    .cutThruAll()

# Feature 4: Apply fillet to sharp top edges of hat channel ridge
step4 = step3.edges("|Z").fillet(1.5)

# Feature 5: Apply edge fillet to bottom perimeter of base for smooth handling
result = step4.edges("#Z").fillet(1)