# Part Metadata
# Part Number: 6776
# Part Name: vented split
# Version: 1
# Timestamp UTC: 20251218_033700
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular extrusion for the split part
step0 = cq.Workplane("XY").box(60, 40, 5)
step1 = step0.faces(">Y").workplane(centerOption="CenterOfMass").transformed(offset=(0, 0, 0), rotate=(0, 90, 0)).rect(62, 7).cutThruAll()
step2 = step1.edges("|Z").edges("<X or >X").fillet(1.5)
step3 = step2.edges("|Y").chamfer(0.8)
result = step3