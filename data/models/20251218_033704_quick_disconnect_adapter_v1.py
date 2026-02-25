# Part Metadata
# Part Number: 1046
# Part Name: quick disconnect adapter
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

# Feature 0: Create cylindrical base body (extrusion)
step0 = cq.Workplane("XY").circle(15).extrude(20)

# Feature 1: Add inner bore hole along Z-axis (cut extrusion)
# Face selection and sketch creation are chained as part of the cut feature
step1 = step0.faces(">Z").workplane().circle(10).cutThruAll()

# Feature 2: Create outer hex profile for wrench grip (cut extrusion)
# Adds a larger hexagonal outline to the outer diameter on top face
step2 = step1.faces(">Z").workplane().polygon(6, 28).cutThruAll()

# Feature 3: Drill side hole for quick disconnect pin (through hole cut)
# Positioned radially for pin retention
step3 = step2.faces(">Y").workplane(centerOption="CenterOfMass").move(0, 0).circle(2.5).cutThruAll()

# Feature 4: Add counterbore on one end for seal groove (blind cut)
# Created on bottom face, smaller diameter recess for O-ring
step4 = step3.faces("<Z").workplane().circle(12).extrude(-2)

# Feature 5: Add small fillet to outer top edges for smooth transition
step5 = step4.edges("|Z").edges(">Z").fillet(1)

# Feature 6: Chamfer inner bore entrance for lead-in
# Applied only to the top inner edge of the bore
step6 = step5.edges("<Z").edges("#Z").chamfer(0.5)

# Final result assignment
result = step6