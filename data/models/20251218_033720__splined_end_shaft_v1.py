# Part Metadata
# Part Number: 9884
# Part Name: - splined end shaft
# Version: 1
# Timestamp UTC: 20251218_033720
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 2
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create main shaft body (extrusion)
step0 = cq.Workplane("XY").circle(10).extrude(60)

# Feature 1: Add splined section on one end (extrusion with polygon profile)
step1 = step0.faces(">Z").workplane().polygon(8, 22).extrude(10)

# Feature 2: Create central through hole along shaft axis (cut)
step2 = step1.faces("<Z").workplane().circle(5).cutThruAll()

# Feature 3: Apply fillet to the transition edge between main shaft and splined section
step3 = step2.edges("|Z").fillet(1.5)

# Feature 4: Add chamfer to the outer end face of the splined section
step4 = step3.faces(">Z").edges().chamfer(0.8)

# Feature 5: Add keyway cutout on the main shaft near the splined end
step5 = step4.faces(">Z").workplane(offset=-5).transformed(rotate=(90, 0, 0))\
    .rect(4, 20).cutBlind(-10)

# Final result
result = step5