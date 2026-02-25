# Part Metadata
# Part Number: 11988
# Part Name: square post hollow
# Version: 1
# Timestamp UTC: 20251218_033723
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create outer square base extrusion
step0 = cq.Workplane("XY").box(50, 50, 100)

# Feature 1: Cut out inner hollow section (centered square cut through all)
step1 = step0.faces(">Z").workplane().rect(30, 30).cutThruAll()

# Feature 2: Add fillet to top and bottom outer edges
step2 = step1.edges("|Z").fillet(3)

# Feature 3: Add chamfer to the four vertical inside edges
step3 = step2.edges("<Z").chamfer(2)

# Feature 4: Drill a through hole on the front face, centered horizontally
step4 = step3.faces(">Y").workplane().center(0, 0).circle(5).cutThruAll()

# Final result
result = step4