# Part Metadata
# Part Number: 8335
# Part Name: frame mount plate
# Version: 1
# Timestamp UTC: 20251218_033709
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
step0 = cq.Workplane("XY").box(80, 60, 5)

# Feature 1: Cut central rectangular opening through the plate (cut extrusion)
# Workplane is placed on top face, then a rectangle is cut through all
step1 = step0.faces(">Z").workplane().rect(40, 30).cutThruAll()

# Feature 2: Drill first through hole at top-left mounting position
step2 = step1.faces(">Z").workplane().moveTo(-25, 20).circle(3.5).cutThruAll()

# Feature 3: Drill second through hole at top-right mounting position
step3 = step2.faces(">Z").workplane().moveTo(25, 20).circle(3.5).cutThruAll()

# Feature 4: Drill third through hole at bottom-left mounting position
step4 = step3.faces(">Z").workplane().moveTo(-25, -20).circle(3.5).cutThruAll()

# Feature 5: Drill fourth through hole at bottom-right mounting position
step5 = step4.faces(">Z").workplane().moveTo(25, -20).circle(3.5).cutThruAll()

# Feature 6: Apply fillet to all four long outer vertical edges of the base plate
step6 = step5.edges("|Z and <X").fillet(3)

# Feature 7: Apply chamfer to the top and bottom inner edges of the central opening
# Select inner edges aligned with Z and in the center region, then chamfer
step7 = step6.edges("<Z and |Y").chamfer(2)

# Final result
result = step7