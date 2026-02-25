# Part Metadata
# Part Number: 540
# Part Name: - double c-bracket
# Version: 1
# Timestamp UTC: 20251218_033724
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 2
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base extrusion for first C-bracket
step0 = cq.Workplane("XY").box(60, 40, 10)

# Feature 1: Cut out inner profile of first C-shape (centered cut)
step1 = step0.faces(">Z").workplane().rect(40, 20).cutThruAll()

# Feature 2: Create mirrored C-bracket by adding second extrusion
step2 = step1.union(cq.Workplane("XY").transformed(rotate=(0, 0, 180), offset=(60, 0, 0)).box(60, 40, 10))

# Feature 3: Cut inner profile of second C-shape
# We need to ensure we're working on the correct face and location
step3 = step2.faces(">Z").workplane().moveTo(60, 0).rect(40, 20).cutThruAll()

# Feature 4: Add mounting hole in first bracket (top-left)
step4 = step3.faces(">Z").workplane().moveTo(-20, 10).circle(3).cutThruAll()

# Feature 5: Add mounting hole in first bracket (bottom-left)
step5 = step4.faces(">Z").workplane().moveTo(-20, -10).circle(3).cutThruAll()

# Feature 6: Add mounting hole in second bracket (top-right)
step6 = step5.faces(">Z").workplane().moveTo(80, 10).circle(3).cutThruAll()

# Feature 7: Add mounting hole in second bracket (bottom-right)
step7 = step6.faces(">Z").workplane().moveTo(80, -10).circle(3).cutThruAll()

# Feature 8: Apply fillet to all vertical edges of outer profile
step8 = step7.edges("|Z").fillet(2)

# Feature 9: Add chamfer to top and bottom face edges for both brackets
result = step8.edges("<Z").chamfer(1).edges(">Z").chamfer(1)