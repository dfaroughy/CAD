# Part Metadata
# Part Number: 10415
# Part Name: ring retainer clip
# Version: 1
# Timestamp UTC: 20251218_033704
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: Yes

import cadquery as cq

# Feature 0: Create base cylindrical body
step0 = cq.Workplane("XY").circle(15.0).extrude(3.0)

# Feature 1: Cut central hole through the center
step1 = step0.faces(">Z").workplane().circle(3.5).cutThruAll()

# Feature 2: Cut a single rectangular notch on top face for ring clearance
step2 = step1.faces(">Z").workplane().rect(8.0, 4.0).cutThruAll()

# Final result
result = step2