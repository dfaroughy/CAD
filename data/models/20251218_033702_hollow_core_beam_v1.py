# Part Metadata
# Part Number: 11453
# Part Name: hollow core beam
# Version: 1
# Timestamp UTC: 20251218_033702
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create outer profile of hollow core beam (base extrusion)
step0 = cq.Workplane("XY").box(200, 60, 40)

# Feature 1: Create central hollow core (cut through all in Z)
# Face selection, workplane, and profile are chained as part of this cut feature
step1 = step0.faces(">Z").workplane().rect(180, 40).cutThruAll()

# Feature 2: Add first side hole for weight reduction or utilities
step2 = step1.faces(">Y").workplane(centerOption="CenterOfMass").moveTo(0, 0).circle(10).cutThruAll()

# Feature 3: Add second side hole, symmetrically opposite
step3 = step2.faces(">Y").workplane(centerOption="CenterOfMass").moveTo(0, 20).circle(10).cutThruAll()

# Feature 4: Add third side hole on opposite face using face selection and offset
step4 = step3.faces("<Y").workplane(centerOption="CenterOfMass").moveTo(0, -20).circle(10).cutThruAll()

# Feature 5: Apply fillet to top and bottom edges along length for stress relief
step5 = step4.edges("|Z and <X").fillet(3)

# Feature 6: Apply chamfer to front and back corners along top edge
step6 = step5.edges("|Z and >Y").chamfer(2)

# Feature 7: Add small locating pin hole at one end (drilled along X-axis)
step7 = step6.faces(">X").workplane().moveTo(10, 0).circle(2.5).cutBlind(-60)

# Feature 8: Add counterbore for bolt head on the opposite end
step8 = step7.faces("<X").workplane().moveTo(-10, 0).circle(4).cutBlind(5).circle(6).cutBlind(2)

# Final result
result = step8