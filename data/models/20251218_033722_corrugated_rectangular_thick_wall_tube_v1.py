# Part Metadata
# Part Number: 12483
# Part Name: corrugated rectangular thick-wall tube
# Version: 1
# Timestamp UTC: 20251218_033722
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 2
# Geometry Fix Model: qwen.qwen3-235b-a22b-2507-v1:0
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular thick-wall tube (extruded hollow box)
step0 = cq.Workplane("XY").box(100, 60, 50).faces(">Z").shell(-10)

# Feature 1: Create corrugation profile using a single sketch with multiple rectangular ribs, then extrude
step1 = step0.faces(">Z").workplane(offset=0).moveTo(-40, 0).rect(8, 4) \
    .moveTo(-24, 0).rect(8, 4) \
    .moveTo(-8, 0).rect(8, 4) \
    .moveTo(8, 0).rect(8, 4) \
    .moveTo(24, 0).rect(8, 4).extrude(5)

# Feature 6: Apply fillet to all outer top edges of the corrugations for smooth transition
step6 = step1.edges("|Z").fillet(1.5)

# Feature 7: Add a central through-hole along Y-axis (cut feature)
step7 = step6.faces(">X").workplane().moveTo(0, 0).circle(10).cutThruAll()

# Final result
result = step7