# Part Metadata
# Part Number: 7820
# Part Name: pvc crank handle
# Version: 1
# Timestamp UTC: 20251218_033718
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: Yes

import cadquery as cq

# Feature 0: Create cylindrical handle grip
step0 = cq.Workplane("XY").circle(15).extrude(100)

# Feature 1: Extrude main shaft from one end of the grip
step1 = step0.faces(">Z").workplane().circle(10).extrude(50)

# Feature 2: Cut a simple keyway slot in the shaft end
step2 = step1.faces(">Z").workplane().transformed(rotate=(90, 0, 0)) \
    .rect(6, 15).cutBlind(-10)

# Final result
result = step2