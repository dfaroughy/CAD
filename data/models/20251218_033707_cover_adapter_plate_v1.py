# Part Metadata
# Part Number: 8327
# Part Name: cover adapter plate
# Version: 1
# Timestamp UTC: 20251218_033707
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular extrusion for the adapter plate
step0 = cq.Workplane("XY").box(80, 60, 8)

# Feature 1: Cut central hole through the plate (aligned to top face)
step1 = step0.faces(">Z").workplane().circle(20).cutThruAll()

# Feature 2: Add four mounting holes, counter-bored, patterned in rectangle
step2 = step1.faces(">Z").workplane().pushPoints([(-25, -15), (25, -15), (-25, 15), (25, 15)]).circle(3.5).cutThruAll()

# Feature 3: Add outer chamfer on top and bottom edges of the main perimeter
step3 = step2.edges("|Z").chamfer(1.0)

# Feature 4: Add fillets to the central hole edge for smooth transition
step4 = step3.edges(cq.selectors.DirectionNthSelector(cq.Vector(0, 0, 1), 0)).fillet(1.5)

# Feature 5: Create a small locating pin hole on one side (half-through)
step5 = step4.faces("<X").workplane(centerOption="CenterOfMass").transformed(offset=(0,0,0), rotate=(0,90,0)).circle(2.5).cutBlind(5)

# Final result
result = step5