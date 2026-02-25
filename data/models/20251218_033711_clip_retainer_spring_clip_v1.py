# Part Metadata
# Part Number: 10924
# Part Name: clip retainer spring clip
# Version: 1
# Timestamp UTC: 20251218_033711
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 1
# Geometry Fix Model: qwen.qwen3-235b-a22b-2507-v1:0
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular extrusion for the clip retainer body
step0 = cq.Workplane("XY").box(20, 6, 3)

# Feature 1: Cut out the central U-shaped notch to form the spring clip profile
# Select top face, set workplane, draw profile, and cut through thickness
step1 = step0.faces(">Z").workplane().moveTo(0, -2).rect(8, 4).cutThruAll()

# Feature 2: Add two mounting holes through the base
# Positioned along the length, centered in width
step2 = step1.faces(">Z").workplane().pushPoints([(-6, 0), (6, 0)]).circle(1.25).cutThruAll()

# Feature 3: Create the upward bending arm of the spring clip
# Use a box primitive centered at one end and union it to the main body
step3 = step2.union(cq.Workplane("XY").moveTo(8, 0).box(4, 6, 1.5))

# Feature 4: Taper the end of the spring arm for easier insertion
# Cut a chamfer on the far tip of the extruded arm
step4 = step3.faces(">X").edges("|Y").chamfer(1)

# Feature 5: Apply fillets to sharp edges on the main body for stress relief and aesthetics
# Fillet long edges along the top and bottom of the base
step5 = step4.edges("|Z").fillet(0.5)

# Feature 6: Add fillet at the base of the spring arm to reduce stress concentration
# Fillet the inner edges where the arm meets the body
step6 = step5.edges("|X").edges("<Z").fillet(0.3)

# Final result
result = step6