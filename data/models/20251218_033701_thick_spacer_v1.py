# Part Metadata
# Part Number: 8845
# Part Name: thick spacer
# Version: 1
# Timestamp UTC: 20251218_033701
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create cylindrical base extrusion for spacer
step0 = cq.Workplane("XY").circle(20).extrude(15)

# Feature 1: Cut central through hole along Z-axis
# Face selection and workplane setup are chained as part of the hole feature
step1 = step0.faces(">Z").workplane().circle(8).cutThruAll()

# Feature 2: Cut first counterbored hole pattern (top face, 4 holes)
step2 = step1.faces(">Z").workplane().pushPoints([(15, 15), (-15, 15), (-15, -15), (15, -15)]).circle(2.5).cboreHole(5, 3, 1.5)

# Feature 3: Add fillet to outer cylindrical edge
step3 = step2.edges("|Z").fillet(1.0)

# Feature 4: Add chamfer to top rim edge (inner hole)
step4 = step3.edges(cq.selectors.DirectionMinMaxSelector(cq.Vector(0, 0, 1), cq.Vector(0, 0, 1))).chamfer(0.8)

# Feature 5: Add chamfer to bottom rim edge (inner hole)
step5 = step4.edges(cq.selectors.DirectionMinMaxSelector(cq.Vector(0, 0, -1), cq.Vector(0, 0, -1))).chamfer(0.8)

# Final result
result = step5