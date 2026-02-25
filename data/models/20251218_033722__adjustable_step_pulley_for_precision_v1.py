# Part Metadata
# Part Number: 10940
# Part Name: - adjustable step pulley for precision
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

# Feature 0: Create base cylinder for the smallest pulley step
step0 = cq.Workplane("XY").circle(15).extrude(10)

# Feature 1: Add second step with larger diameter (stacked extrusion)
step1 = step0.faces(">Z").workplane().circle(20).extrude(8)

# Feature 2: Add third step with even larger diameter (stacked extrusion)
step2 = step1.faces(">Z").workplane().circle(25).extrude(6)

# Feature 3: Add fourth step with larger diameter (stacked extrusion)
step3 = step2.faces(">Z").workplane().circle(30).extrude(4)

# Feature 4: Add central bore hole through entire pulley (cut)
step4 = step3.faces("<Z").workplane().circle(5).cutThruAll()

# Feature 5: Add keyway slot for shaft locking (cut)
step5 = step4.faces("<Z").workplane().center(-7, 0).box(4, 14, 12, centered=(True, True, False))

# Feature 6: Chamfer top edges of each step for deburring and assembly
step6 = step5.edges("|Z").chamfer(1)

# Feature 7: Fillet between steps to reduce stress concentration
step7 = step6.edges("|Z").fillet(1.5)

# Final result
result = step7