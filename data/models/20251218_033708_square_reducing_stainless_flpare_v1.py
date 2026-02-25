# Part Metadata
# Part Number: 3132
# Part Name: square reducing stainless flpare
# Version: 1
# Timestamp UTC: 20251218_033708
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create large base square flange (extrusion)
step0 = cq.Workplane("XY").box(100, 100, 10)

# Feature 1: Extrude smaller square on top to form reduction step (additive extrusion)
# Select top face, create workplane, draw smaller square, extrude upward
step1 = step0.faces(">Z").workplane().rect(60, 60).extrude(10)

# Feature 2: Add central through hole for bore (cut extrusion)
# Performed on the top face of the second extrusion
step2 = step1.faces(">Z").workplane().circle(20).cutThruAll()

# Feature 3: Add four mounting holes, counter-sunk through both flange sections (cut pattern)
# Select top face, define hole pattern locations, create through holes
step3 = step2.faces(">Z").workplane().rect(80, 80, forConstruction=True).vertices().circle(5).cutThruAll()

# Feature 4: Apply fillet to outer edge of base flange (edge modification)
step4 = step3.edges("|Z").edges("<Y").fillet(3)

# Feature 5: Apply fillet to outer edge of top reduced square (edge modification)
step5 = step4.edges("|Z").edges(">Y").fillet(2)

# Feature 6: Chamfer inner bore edge on both top and bottom faces (edge modification)
step6 = step5.edges("<Z").edges("#Z").chamfer(1)

# Final result
result = step6