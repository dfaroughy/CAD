# Part Metadata
# Part Number: 2091
# Part Name: dowel pin with hex head
# Version: 1
# Timestamp UTC: 20251218_033705
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create hex head (extrusion)
step0 = cq.Workplane("XY").polygon(6, 10).extrude(6)

# Feature 1: Create cylindrical shaft (extrusion)
step1 = step0.faces(">Z").workplane().circle(3).extrude(20)

# Feature 2: Add chamfer to top edge of hex head (modify operation)
step2 = step1.faces("<Z").edges().chamfer(0.5)

# Feature 3: Add fillet at junction between hex head and shaft (modify operation)
step3 = step2.faces(">Z").edges("<Z").fillet(1)

# Feature 4: Add slot in hex head (cut extrusion)
step4 = step3.faces(">Z").workplane().rect(8, 2).cutThruAll()

# Final result
result = step4