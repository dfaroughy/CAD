# Part Metadata
# Part Number: 8332
# Part Name: perforated mount plate
# Version: 1
# Timestamp UTC: 20251218_033710
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular plate (extrusion)
step0 = cq.Workplane("XY").box(120, 80, 5)

# Feature 1: Add first through hole at center (cut extrusion)
# Face selection and profile creation are chained as part of the feature
step1 = step0.faces(">Z").workplane().circle(8).cutThruAll()

# Feature 2: Add second through hole along X-axis (cut extrusion)
step2 = step1.faces(">Z").workplane().moveTo(40, 0).circle(6).cutThruAll()

# Feature 3: Add third through hole symmetric on negative X-axis (cut extrusion)
step3 = step2.faces(">Z").workplane().moveTo(-40, 0).circle(6).cutThruAll()

# Feature 4: Add fourth through hole along Y-axis (cut extrusion)
step4 = step3.faces(">Z").workplane().moveTo(0, 30).circle(6).cutThruAll()

# Feature 5: Add fifth through hole symmetric on negative Y-axis (cut extrusion)
step5 = step4.faces(">Z").workplane().moveTo(0, -30).circle(6).cutThruAll()

# Feature 6: Apply fillet to all vertical edges of the base plate (edge fillet)
step6 = step5.edges("|Z").fillet(3)

# Feature 7: Add chamfer to top and bottom edges of the central hole (chamfer on hole edges)
# Select inner cylindrical face of the main hole and chamfer its top and bottom edges
step7 = step6.faces("#Z").edges().chamfer(1)

# Final result
result = step7