# Part Metadata
# Part Number: 5723
# Part Name: - truncated sphere with notch
# Version: 1
# Timestamp UTC: 20251218_033658
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create truncated sphere base using sphere operation with angle limits
step0 = cq.Workplane("XY").sphere(50, angle1=-60, angle2=60)

# Feature 1: Add a notch by cutting a rectangular extrusion through the sphere along equator
step1 = step0.faces(">Z").workplane(offset=0).transformed(rotate=(90, 0, 0)) \
        .rect(30, 10).cutThruAll()

# Feature 2: Apply fillet to the notch edges to smooth sharp corners
result = step1.edges(cq.selectors.NearestToPointSelector((0, 0, 0))).fillet(2)