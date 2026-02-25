# Part Metadata
# Part Number: 11465
# Part Name: hollow square column
# Version: 1
# Timestamp UTC: 20251218_033724
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create outer square profile and extrude to form base column
step0 = cq.Workplane("XY").box(50, 50, 100)

# Feature 1: Create inner square cutout to make column hollow (cut extrusion)
# Workplane on top face, draw inner square, cut through all thickness
step1 = step0.faces(">Z").workplane().rect(40, 40).cutThruAll()

# Feature 2: Apply fillet to outer top and bottom edges of the column
# Select vertical outer edges and apply fillet
step2 = step1.edges("|Z and <X or |Z and >X or |Z and <Y or |Z and >Y").fillet(3)

# Feature 3: Add a rectangular cutout on the front face for access
# Select front face, position workplane, draw rectangle, and cut through thickness
step3 = step2.faces(">Y").workplane().rect(20, 30).cutThruAll()

# Feature 4: Add through-hole pattern on top face (two holes along X-axis)
# Position on top face, define two hole centers, and drill through
step4 = step3.faces(">Z").workplane().pushPoints([(-15, 0), (15, 0)]).circle(2.5).cutThruAll()

# Final result
result = step4