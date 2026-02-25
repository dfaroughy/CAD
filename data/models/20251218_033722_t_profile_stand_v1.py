# Part Metadata
# Part Number: 11987
# Part Name: t-profile stand
# Version: 1
# Timestamp UTC: 20251218_033722
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base T-profile extrusion (vertical stem)
step0 = cq.Workplane("XY").box(20, 60, 10)

# Feature 1: Add top crossbar of T (extrusion on top face)
step1 = step0.faces(">Z").workplane().rect(40, 10).extrude(10)

# Feature 2: Chamfer top edges of crossbar for aesthetics (chamfer operation)
step2 = step1.edges("|Z and >Y").chamfer(2)

# Feature 3: Add central mounting hole through entire part (cut feature)
step3 = step1.faces(">Z").workplane(centerOption="CenterOfMass").circle(5).cutThruAll()

# Feature 4: Add two countersunk screw clearance holes in base plate (patterned cut)
step4 = step3.faces("<Z").workplane().pushPoints([(-15, 0), (15, 0)]).circle(3.5).cutThruAll()

# Feature 5: Apply fillet to bottom base edges for strength and handling (edge fillet)
step5 = step4.edges("<Z").fillet(1)

# Final result
result = step5