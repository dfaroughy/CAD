# Part Metadata
# Part Number: 2083
# Part Name: titanium screw
# Version: 1
# Timestamp UTC: 20251218_033722
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 3
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create cylindrical screw shaft (extrusion)
step0 = cq.Workplane("XY").circle(2.5).extrude(40)

# Feature 1: Add screw head (extrusion on top face)
step1 = step0.faces(">Z").workplane().circle(4).extrude(3)

# Feature 2: Cut hexagonal socket in screw head (cut extrusion)
step2 = step1.faces(">Z").workplane().polygon(6, 3).cutThruAll()

# Feature 3: Simulate thread by cutting a cylinder from the top
step3 = step2.faces(">Z").workplane().circle(2.2).cutBlind(-35)

# Feature 4: Chamfer top edge of screw head for aesthetics
step4 = step3.faces(">Z").edges().chamfer(0.5)

# Feature 5: Fillet base where head meets shaft for stress relief
step5 = step4.edges("|Z").edges("<Z").fillet(1)

# Feature 6: Add fillet at tip of screw for smooth entry
step6 = step5.faces("<Z").edges().fillet(0.3)

# Final result
result = step6