# Part Metadata
# Part Number: 22
# Part Name: thick-wall cable bracket
# Version: 1
# Timestamp UTC: 20251218_033719
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create main bracket base (extrusion)
step0 = cq.Workplane("XY").box(60, 40, 15)

# Feature 1: Create cable pass-through cutout (centered cut extrusion)
# Includes face selection, workplane, and profile definition as part of the feature
step1 = step0.faces(">Z").workplane().rect(30, 20).cutThruAll()

# Feature 2: Add mounting hole on left side (cut)
step2 = step1.faces(">Z").workplane().workplane(offset=0).moveTo(-15, 0).circle(3.5).cutThruAll()

# Feature 3: Add mounting hole on right side (cut)
step3 = step2.faces(">Z").workplane().workplane(offset=0).moveTo(15, 0).circle(3.5).cutThruAll()

# Feature 4: Add top fillet to improve cable bending radius (edge fillet)
step4 = step3.edges("|Z and <X").fillet(5)

# Feature 5: Add bottom edge fillets for structural reinforcement (edge fillet)
step5 = step4.edges("|Z and >X").fillet(3)

# Feature 6: Add corner chamfers on front and back vertical edges (chamfer)
step6 = step5.edges("|Y").chamfer(2)

# Final result
result = step6