# Part Metadata
# Part Number: 6777
# Part Name: - panel
# Version: 1
# Timestamp UTC: 20251218_033657
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base panel (extrusion)
step0 = cq.Workplane("XY").box(120, 80, 5)

# Feature 1: Add central through hole (cut)
step1 = step0.faces(">Z").workplane().circle(10).cutThruAll()

# Feature 2: Add four corner holes (cut pattern)
step2 = step1.faces(">Z").workplane().pushPoints([(30, 30), (30, -30), (-30, 30), (-30, -30)]).circle(4).cutThruAll()

# Feature 3: Add edge fillets on top and bottom edges (modify operation)
step3 = step2.edges("|Z").fillet(3)

# Feature 4: Add two side cutouts (rectangular pocket)
step4 = step3.faces(">Y").workplane(centerOption="CenterOfMass").transformed(rotate=(0, 90, 0)).rect(40, 20).cutThruAll()

# Feature 5: Add chamfer to front and back edges
result = step4.edges("<X or >X").chamfer(2)