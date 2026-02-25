# Part Metadata
# Part Number: 5224
# Part Name: pyramid with notches
# Version: 1
# Timestamp UTC: 20251218_033717
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create pyramid base (a square) and extrude into a pyramid using a tapered extrusion
step0 = cq.Workplane("XY").rect(50, 50).workplane(offset=25).rect(0.1, 0.1).loft(combine=True)

# Feature 1: Cut first notch on the front face (along +Y edge)
# Select front face, create workplane, draw rectangle for notch, cut through all
step1 = step0.faces(">Y").workplane(centerOption="CenterOfMass").moveTo(0, 0).box(10, 0.1, 5, centered=(True, True, False), combine="cut")

# Feature 2: Cut second notch on the back face (along -Y edge)
# Select back face, create workplane, draw rectangle for notch, cut through all
step2 = step1.faces("<Y").workplane(centerOption="CenterOfMass").moveTo(0, 0).box(10, 0.1, 5, centered=(True, True, False), combine="cut")

# Feature 3: Cut third notch on the right face (along +X edge)
# Select right face, create workplane, draw rectangle for notch, cut through all
step3 = step2.faces(">X").workplane(centerOption="CenterOfMass").moveTo(0, 0).box(0.1, 10, 5, centered=(True, True, False), combine="cut")

# Feature 4: Cut fourth notch on the left face (along -X edge)
# Select left face, create workplane, draw rectangle for notch, cut through all
step4 = step3.faces("<X").workplane(centerOption="CenterOfMass").moveTo(0, 0).box(0.1, 10, 5, centered=(True, True, False), combine="cut")

# Final result
result = step4