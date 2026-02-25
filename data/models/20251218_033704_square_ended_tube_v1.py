# Part Metadata
# Part Number: 12500
# Part Name: square-ended tube
# Version: 1
# Timestamp UTC: 20251218_033704
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create outer square profile and extrude to form base tube (extrusion)
step0 = cq.Workplane("XY").box(50, 50, 100)

# Feature 1: Create inner square cutout to form hollow tube (cut extrusion)
# Note: workplane, face selection, and inner profile are part of this feature
step1 = step0.faces(">Z").workplane().rect(40, 40).cutThruAll()

# Feature 2: Add fillets on the four top outer edges (modify operation)
step2 = step1.edges("|Z and >Y").fillet(3)

# Feature 3: Add fillets on the four bottom outer edges (modify operation)
step3 = step2.edges("|Z and <Y").fillet(3)

# Feature 4: Drill a through hole on the front face (cut extrusion)
step4 = step3.faces(">Y").workplane().circle(5).cutThruAll()

# Feature 5: Apply chamfer to all four long outer vertical edges (modify operation)
step5 = step4.edges("|Z").edges("%LINE").chamfer(2)

# Final result
result = step5