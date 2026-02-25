# Part Metadata
# Part Number: 7812
# Part Name: brass spacer tube
# Version: 1
# Timestamp UTC: 20251218_033650
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create cylindrical base extrusion for spacer tube (outer diameter)
step0 = cq.Workplane("XY").circle(6.0).extrude(10.0)

# Feature 1: Cut inner bore (hole through center for shaft or screw)
step1 = step0.faces(">Z").workplane().circle(4.0).cutThruAll()

# Feature 2: Apply fillet to top outer edge
step2 = step1.edges(cq.selectors.DirectionMinMaxSelector(cq.Vector(0, 0, 1), cq.Vector(0, 0, 1))).fillet(0.5)

# Feature 3: Apply fillet to bottom outer edge
step3 = step2.edges(cq.selectors.DirectionMinMaxSelector(cq.Vector(0, 0, -1), cq.Vector(0, 0, -1))).fillet(0.5)

# Final result
result = step3