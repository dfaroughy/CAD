# Part Metadata
# Part Number: 8345
# Part Name: reinforcement spacer square plate
# Version: 1
# Timestamp UTC: 20251218_033723
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base square plate (extrusion)
step0 = cq.Workplane("XY").box(80, 80, 10)

# Feature 1: Cut central square opening (cut extrusion)
# Face selection, workplane, and profile defined inline with the cut operation
step1 = step0.faces(">Z").workplane().rect(30, 30).cutThruAll()

# Feature 2: Drill four corner holes (patterned cut)
# Single hole defined and then circular pattern applied as one feature operation
step2 = step1.faces(">Z").workplane().pushPoints([(25, 25), (25, -25), (-25, 25), (-25, -25)]).circle(5).cutThruAll()

# Feature 3: Add fillets on outer vertical edges (edge fillet operation)
step3 = step2.edges("|Z and <X and <Y").fillet(3)

# Feature 4: Add chamfer on top outer perimeter (chamfer operation)
step4 = step3.edges("|Z").edges(">Z").chamfer(2)

# Feature 5: Add small fillets on inner square cut edges (fillet on internal edges)
step5 = step4.edges(cq.selectors.NearestToPointSelector((0, 0, 0))).fillet(1.5)

# Final result assignment
result = step5