# Part Metadata
# Part Number: 5207
# Part Name: hollow cube
# Version: 1
# Timestamp UTC: 20251218_033656
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create outer cube (base extrusion)
step0 = cq.Workplane("XY").box(50, 50, 50)

# Feature 1: Create inner hollow cavity (cut extrusion)
# Workplane and inner profile are part of this cut feature
step1 = step0.faces(">Z").workplane(offset=0).rect(40, 40).cutThruAll()

# Feature 2: Apply fillet to all external edges of the hollow cube
result = step1.edges("|Z").fillet(3)