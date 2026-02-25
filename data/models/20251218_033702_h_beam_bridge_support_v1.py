# Part Metadata
# Part Number: 11455
# Part Name: h-beam bridge support
# Version: 1
# Timestamp UTC: 20251218_033702
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular flange (extrusion for bottom flange)
step0 = cq.Workplane("XY").box(80, 10, 5)

# Feature 1: Add vertical web (extrusion on top of bottom flange)
step1 = step0.faces(">Z").workplane().box(10, 10, 20, centered=(True, True, False))

# Feature 2: Add top flange (extrusion on top of web)
step2 = step1.faces(">Z").workplane().box(80, 10, 5, centered=(True, True, False))

# Feature 3: Fillet the inner vertical edges between web and top flange
step3 = step2.edges("|Z and <Y").fillet(2)

# Feature 4: Fillet the inner vertical edges between web and bottom flange
step4 = step3.edges("|Z and >Y").fillet(2)

# Feature 5: Cut a centered circular hole through the web in the XY plane
step5 = step4.faces(">Y").workplane().transformed(offset=(0, 0, 0), rotate=(90, 0, 0)) \
         .circle(6).cutThruAll()

# Feature 6: Add four mounting holes in the bottom flange, counter-bored
step6 = step5.faces("<Z").workplane() \
         .pushPoints([(-30, -5), (30, -5), (-30, 5), (30, 5)]) \
         .cskHole(6, 8, 90)

# Feature 7: Add two through-holes in the top flange for assembly
step7 = step6.faces(">Z").workplane() \
         .pushPoints([(-20, 0), (20, 0)]) \
         .circle(4).cutThruAll()

# Final result
result = step7