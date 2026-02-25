# Part Metadata
# Part Number: 541
# Part Name: tabs bracket
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

# Feature 0: Create main bracket base (extrusion)
step0 = cq.Workplane("XY").box(60, 40, 5)

# Feature 1: Add vertical tab on front edge (extrusion)
step1 = step0.faces(">Y").workplane(centerOption="CenterOfMass").rect(10, 5).extrude(15)

# Feature 2: Add mounting hole in base plate (cut)
step2 = step1.faces("<Z").workplane().move(15, 15).circle(3).cutThruAll()

# Feature 3: Add second mounting hole in base plate (cut)
step3 = step2.faces("<Z").workplane().move(-15, 15).circle(3).cutThruAll()

# Feature 4: Add through hole in vertical tab (cut)
step4 = step3.faces(">Z").workplane(offset=10).move(0, 7.5).circle(2.5).cutThruAll()

# Feature 5: Round top front edge of vertical tab (fillet)
step5 = step4.edges("|Y and >Z").fillet(2)

# Feature 6: Chamfer four corners of base plate (chamfer)
step6 = step5.edges("|Z").edges("<X or >X or <Y or >Y").chamfer(1)

# Final result
result = step6