# Part Metadata
# Part Number: 10927
# Part Name: step pulley with keyway
# Version: 1
# Timestamp UTC: 20251218_033701
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base cylinder for the largest pulley step (extrusion)
step0 = cq.Workplane("XY").circle(25).extrude(10)

# Feature 1: Add second step (smaller diameter, centered on top)
step1 = step0.faces(">Z").workplane().circle(20).extrude(8)

# Feature 2: Add third step (even smaller, centered on top)
step2 = step1.faces(">Z").workplane().circle(15).extrude(6)

# Feature 3: Add fourth step (smallest, centered on top)
step3 = step2.faces(">Z").workplane().circle(10).extrude(4)

# Feature 4: Create central shaft hole through entire pulley (cut)
step4 = step3.faces("<Z").workplane().circle(5).cutThruAll()

# Feature 5: Add keyway slot using a rectangular cut (cut extrusion)
# Position the keyway along the X-axis on the central hole face
step5 = step4.faces("<Z").workplane().transformed(offset=(0, 0, 0), rotate=(90, 0, 0)) \
           .rect(3, 10).cutThruAll()

# Feature 6: Apply fillets to the edges between each pulley step (modify operation)
# Fillet the outer vertical edges where steps meet
step6 = step5.edges("|Z").fillet(1)

# Feature 7: Apply chamfer to the top edge of the smallest step for deburring
step7 = step6.faces(">Z").edges().chamfer(0.5)

# Final result
result = step7