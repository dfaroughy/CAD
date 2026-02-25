# Part Metadata
# Part Number: 10930
# Part Name: precision wedge cam
# Version: 1
# Timestamp UTC: 20251218_033718
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 2
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular block for the wedge cam
step0 = cq.Workplane("XY").box(60, 30, 15)

# Feature 1: Create the precision wedge ramp profile via a cut on the top face
# Select top face, set workplane, draw trapezoidal ramp sketch, and cut
step1 = step0.faces(">Z").workplane().polyline([(0, 0), (20, 0), (40, 10), (60, 10), (60, 0)]).close().cutThruAll()

# Feature 2: Add a central through-hole for the shaft
# Position hole at center of part, normal to top face, cut through entire part
step2 = step1.faces(">Z").workplane().circle(5).cutThruAll()

# Feature 3: Add a mounting hole pattern (two holes along X-axis on bottom face)
# Select bottom face, create two holes using a rectangular pattern
step3 = step2.faces("<Z").workplane().rect(40, 20).vertices().circle(3).extrude(-15)

# Feature 4: Apply fillet to the sharp edges of the wedge ramp for smooth transition
# Select only the top front and top sloped edges of the ramp
step4 = step3.edges(cq.selectors.NearestToPointSelector((50, 0, 7.5))).fillet(2)

# Feature 5: Apply edge chamfer to the base perimeter on the top face for assembly clearance
# Select all vertical edges on the top perimeter
step5 = step4.edges("|Z and >X").chamfer(1)

# Final result
result = step5