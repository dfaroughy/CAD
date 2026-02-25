# Part Metadata
# Part Number: 1063
# Part Name: male thread adapter
# Version: 1
# Timestamp UTC: 20251218_033723
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create cylindrical base for the male thread adapter (extrusion)
step0 = cq.Workplane("XY").circle(10).extrude(20)

# Feature 1: Add a smaller diameter section for threading (extrusion on top face)
step1 = step0.faces(">Z").workplane().circle(8).extrude(15)

# Feature 2: Cut a through hole for the internal bore (cut extrusion)
step2 = step1.faces(">Z").workplane().circle(5).cutThruAll()

# Feature 3: Add external thread profile using a helical cut (simulated with a rectangular cut revolve)
# Note: CadQuery does not support true helical sweeps in standard operations, so we simulate with a shallow angled cut
# Using a trapezoidal profile cut rotated slightly to mimic one turn of thread start
step3 = step2.faces(">Z").workplane().transformed(offset=(0, 0, -1), rotate=(45, 0, 0)) \
    .rect(1.5, 0.5).cutThruAll()

# Feature 4: Apply chamfer to the tip of the threaded end for ease of assembly
step4 = step3.faces(">Z").edges().chamfer(0.5)

# Feature 5: Add a hexagonal feature near the base for wrench grip (extrusion)
step5 = step0.faces("<Z").workplane().polygon(6, 18).extrude(5)

# Feature 6: Combine the hex base with the main body (boolean union)
step6 = step5.union(step4)

# Feature 7: Apply fillet to the bottom edges of the hex feature for smoother transition
step7 = step6.edges("|Z").edges("<Z").fillet(1)

# Final result
result = step7