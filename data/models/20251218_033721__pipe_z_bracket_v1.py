# Part Metadata
# Part Number: 23
# Part Name: - pipe z-bracket
# Version: 1
# Timestamp UTC: 20251218_033721
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base vertical plate (extrusion)
step0 = cq.Workplane("XY").box(10, 50, 5)
step1 = step0.faces("<Y").workplane(centerOption="CenterOfMass").transformed(offset=(0, 0, -25), rotate=(90, 0, 0)).box(10, 50, 5, centered=(True, True, False))
step2 = step1.faces(">Z").workplane().moveTo(5, 25).circle(3).cutThruAll()
step3 = step2.edges("|Y and >Z").fillet(2)
step4 = step3.edges("|Y and <X").fillet(2)
result = step4