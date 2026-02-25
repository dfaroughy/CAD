# Part Metadata
# Part Number: 7811
# Part Name: standoff spacer type
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

# Feature 0: Create cylindrical base extrusion for standoff spacer
step0 = cq.Workplane("XY").circle(6).extrude(10)

# Feature 1: Cut central through-hole for screw (cut extrusion)
# Face selection and profile creation chained as part of this cut feature
step1 = step0.faces(">Z").workplane().circle(2.5).cutThruAll()

# Feature 2: Create outer chamfer on top edge (chamfer feature)
step2 = step1.edges(">Z").chamfer(0.5)

# Feature 3: Create outer chamfer on bottom edge (chamfer feature)
step3 = step2.edges("<Z").chamfer(0.5)

# Feature 4: Add fillet to inner hole edge at top (fillet feature)
step4 = step3.edges(cq.selectors.NearestToPointSelector((0, 0, 9.5))).fillet(0.3)

# Feature 5: Add fillet to inner hole edge at bottom (fillet feature)
step5 = step4.edges(cq.selectors.NearestToPointSelector((0, 0, 0.5))).fillet(0.3)

# Final result
result = step5