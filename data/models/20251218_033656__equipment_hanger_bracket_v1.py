# Part Metadata
# Part Number: 14
# Part Name: - equipment hanger bracket
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

# Feature 0: Create base rectangular plate (extrusion)
step0 = cq.Workplane("XY").box(60, 40, 5)

# Feature 1: Extrude hanger arm upward from front edge (pad/extrusion)
step1 = step0.faces(">Y").workplane(centerOption="CenterOfMass").moveTo(0, 0).rect(20, 8).extrude(25)

# Feature 2: Cut central slot in hanger arm (cut extrusion)
step2 = step1.faces(">Z").workplane(centerOption="CenterOfMass").moveTo(0, 5).rect(6, 16).cutThruAll()

# Feature 3: Cut mounting holes in base plate (through holes)
step3 = step2.faces("<Z").workplane().rect(40, 30, forConstruction=True).vertices().circle(3).cutThruAll()

# Feature 4: Fillet bottom edges of base plate for smoother appearance
step4 = step3.edges("|Z and <Y").fillet(2)

# Feature 5: Chamfer top front edges of hanger arm for aesthetics and deburring
result = step4.edges("|Z and >Y").chamfer(1.5)