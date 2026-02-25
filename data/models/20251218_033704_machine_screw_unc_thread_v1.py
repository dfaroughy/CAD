# Part Metadata
# Part Number: 2615
# Part Name: machine screw unc thread
# Version: 1
# Timestamp UTC: 20251218_033704
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create cylindrical screw shank (extrusion)
step0 = cq.Workplane("XY").circle(2.5).extrude(20)

# Feature 1: Add threaded portion using a smaller diameter cylinder (extrusion)
# Note: Approximate thread as smooth cylinder; true helical threads require advanced modeling
step1 = step0.faces(">Z").workplane().circle(2.3).extrude(10)

# Feature 2: Create flat screw head (larger diameter extrusion on top)
step2 = step1.faces(">Z").workplane().circle(4).extrude(2)

# Feature 3: Cut slot for flat-head screwdriver (rectangular cut through head)
step3 = step2.faces(">Z").workplane().rect(0.5, 3).cutThruAll()

# Feature 4: Chamfer top edge of screw head for realism
step4 = step3.faces(">Z").edges().chamfer(0.3)

# Feature 5: Add root fillet at base of head where it meets shank
step5 = step4.faces(">Z").edges("<Z").fillet(0.2)

# Feature 6: Add small chamfer at tip of screw for realism
step6 = step5.faces("<Z").edges().chamfer(0.2)

# Final result
result = step6