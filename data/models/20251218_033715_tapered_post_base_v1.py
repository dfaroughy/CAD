# Part Metadata
# Part Number: 11975
# Part Name: tapered post base
# Version: 1
# Timestamp UTC: 20251218_033715
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create tapered post base main body using a rectangular extrusion with taper (loft)
step0 = cq.Workplane("XY").rect(60, 60).workplane(offset=80).rect(40, 40).loft(combine=True)

# Feature 1: Add mounting base flange at the bottom (extrusion on bottom face)
step1 = step0.faces("<Z").workplane().rect(70, 70).extrude(10)

# Feature 2: Cut central through hole for post or fastener (cut extrusion)
step2 = step1.faces(">Z").workplane().circle(15).cutThruAll()

# Feature 3: Add four countersunk mounting holes, patterned in a rectangle (hole cut + pattern)
step3 = step2.faces("<Z").workplane().pushPoints([(-25, -25), (25, -25), (25, 25), (-25, 25)]).cskHole(5, 8, 90)

# Feature 4: Apply fillet to the base top edge where flange meets tapered body (edge fillet)
step4 = step3.edges("|Z").edges("<Z").fillet(3)

# Feature 5: Apply chamfer to the top outer edges of the taper for deburring (chamfer)
step5 = step4.edges(">Z").chamfer(2)

# Final result
result = step5