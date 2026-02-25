# Part Metadata
# Part Number: 2102
# Part Name: taper pin - stainless
# Version: 1
# Timestamp UTC: 20251218_033721
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Create a tapered cylinder using loft between two circles of different radii
step0 = cq.Workplane("XY").circle(5).workplane(offset=50).circle(4).loft()

# Chamfer the bottom edge (thick end) by selecting edges on the bottom face
step1 = step0.faces("<Z").edges().chamfer(0.5)

# Fillet the top edge (thin end) by selecting edges on the top face
step2 = step1.faces(">Z").edges().fillet(0.3)

# Final result assignment
result = step2