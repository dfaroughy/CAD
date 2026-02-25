# Part Metadata
# Part Number: 1
# Part Name: corner bracket with angle adjustment
# Version: 1
# Timestamp UTC: 20251218_033723
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 2
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create main L-shaped bracket base (extrusion)
step0 = cq.Workplane("XY").box(60, 60, 8)

# Feature 1: Cut out inner corner to form L-shape walls (cut extrusion)
step1 = step0.faces(">Z").workplane().move(-15, -15).box(30, 30, 10, centered=(True, True, True), combine="cut")

# Feature 2: Add mounting hole in first arm (through hole cut)
step2 = step1.faces(">Z").workplane().move(15, -30).circle(3.5).cutThruAll()

# Feature 3: Add mounting hole in second arm (through hole cut)
step3 = step2.faces(">Z").workplane().move(-30, 15).circle(3.5).cutThruAll()

# Feature 4: Create slot for angle adjustment in first arm (rectangular cut)
step4 = step3.faces(">Z").workplane().move(15, -20).slot2D(20, 6, angle=90).cutThruAll()

# Feature 5: Create slot for angle adjustment in second arm (rectangular cut)
step5 = step4.faces(">Z").workplane().move(-20, 15).slot2D(20, 6, angle=0).cutThruAll()

# Feature 6: Apply fillet to all external edges of the bracket (edge fillet)
step6 = step5.edges("|Z").fillet(2)

# Feature 7: Add chamfer to top and bottom edges around the central cutout (chamfer operation)
# Select inner vertical edges from the corner cutout and chamfer them
step7 = step6.faces("<Z").edges("%Circle").chamfer(1)

# Final result
result = step7