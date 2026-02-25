# Part Metadata
# Part Number: 8331
# Part Name: square spaced plate
# Version: 1
# Timestamp UTC: 20251218_033659
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base square plate (extrusion)
step0 = cq.Workplane("XY").box(100, 100, 10)

# Feature 1: Cut first through hole at bottom-left quadrant
step1 = step0.faces(">Z").workplane().transformed(offset=cq.Vector(-25, -25, 0)).circle(5).cutThruAll()

# Feature 2: Cut second through hole at bottom-right quadrant
step2 = step1.faces(">Z").workplane().transformed(offset=cq.Vector(25, -25, 0)).circle(5).cutThruAll()

# Feature 3: Cut third through hole at top-right quadrant
step3 = step2.faces(">Z").workplane().transformed(offset=cq.Vector(25, 25, 0)).circle(5).cutThruAll()

# Feature 4: Cut fourth through hole at top-left quadrant
step4 = step3.faces(">Z").workplane().transformed(offset=cq.Vector(-25, 25, 0)).circle(5).cutThruAll()

# Feature 5: Apply fillet to all vertical edges of the plate
result = step4.edges("|Z").fillet(3)