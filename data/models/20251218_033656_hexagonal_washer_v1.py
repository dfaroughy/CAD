# Part Metadata
# Part Number: 2096
# Part Name: hexagonal washer
# Version: 1
# Timestamp UTC: 20251218_033656
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create outer hexagonal base (extrusion)
step0 = cq.Workplane("XY").polygon(6, 20.0).extrude(3.0)

# Feature 1: Cut central circular hole through the washer (cut extrusion)
# Face selection and hole profile are chained as part of the cut feature
step1 = step0.faces(">Z").workplane().circle(5.0).cutThruAll()

# Feature 2: Apply fillet to top and bottom outer edges for smooth finish
step2 = step1.edges("|Z").fillet(1.0)

# Final result
result = step2