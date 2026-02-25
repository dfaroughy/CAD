# Part Metadata
# Part Number: 8866
# Part Name: tinned plate
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

# Feature 0: Create base tinned plate (extruded rectangular prism)
step0 = cq.Workplane("XY").box(80, 60, 3)

# Feature 1: Add four mounting holes as through cuts (cut extrusion)
# Face selection, workplane, and circular profiles are part of this feature
step1 = step0.faces(">Z").workplane().pushPoints([(-25, -20), (25, -20), (-25, 20), (25, 20)]).circle(3).cutThruAll()

# Feature 2: Add edge fillet along all vertical edges of the plate
step2 = step1.edges("|Z").fillet(1.5)

# Feature 3: Add small chamfer on top and bottom perimeter edges to simulate tinning radius
step3 = step2.edges("<Z or >Z").chamfer(0.3)

# Final result
result = step3