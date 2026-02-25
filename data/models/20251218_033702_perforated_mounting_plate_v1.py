# Part Metadata
# Part Number: 8336
# Part Name: perforated mounting plate
# Version: 1
# Timestamp UTC: 20251218_033702
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular plate (extrusion)
step0 = cq.Workplane("XY").box(80, 60, 5)

# Feature 1: Cut central rectangular hole through the plate
step1 = step0.faces(">Z").workplane().rect(40, 30).cutThruAll()

# Feature 2: Drill first through hole in top-left corner
step2 = step1.faces(">Z").workplane().moveTo(30, 20).circle(3).cutThruAll()

# Feature 3: Drill second through hole in top-right corner
step3 = step2.faces(">Z").workplane().moveTo(-30, 20).circle(3).cutThruAll()

# Feature 4: Drill third through hole in bottom-right corner
step4 = step3.faces(">Z").workplane().moveTo(-30, -20).circle(3).cutThruAll()

# Feature 5: Drill fourth through hole in bottom-left corner
step5 = step4.faces(">Z").workplane().moveTo(30, -20).circle(3).cutThruAll()

# Feature 6: Apply fillet to all vertical edges of the base plate
step6 = step5.edges("|Z").fillet(2)

# Feature 7: Chamfer the outer top and bottom edges of the central rectangular cutout
step7 = step6.edges(cq.selectors.NearestToPointSelector((0, 0, 2.5))).chamfer(1)
step8 = step7.edges(cq.selectors.NearestToPointSelector((0, 0, -2.5))).chamfer(1)

# Final result
result = step8