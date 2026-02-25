# Part Metadata
# Part Number: 12482
# Part Name: beveled thick-wall tube
# Version: 1
# Timestamp UTC: 20251218_033657
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create outer cylindrical base (extrusion)
step0 = cq.Workplane("XY").circle(25).extrude(50)

# Feature 1: Cut inner hole to create thick-wall tube (cut extrusion)
# Face selection and profile are chained as part of the cut feature
step1 = step0.faces(">Z").workplane().circle(20).cutThruAll()

# Feature 2: Bevel the top edge of the tube (chamfer operation)
# Select top edges and apply chamfer as a single feature
step2 = step1.edges(cq.selectors.DirectionMinMaxSelector(cq.Vector(0, 0, 1), cq.Vector(0, 0, 1))).chamfer(2)

# Feature 3: Bevel the bottom edge of the tube (chamfer operation)
# Select bottom edges and apply chamfer as a separate feature
step3 = step2.edges(cq.selectors.DirectionMinMaxSelector(cq.Vector(0, 0, -1), cq.Vector(0, 0, -1))).chamfer(2)

# Final result
result = step3