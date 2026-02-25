# Part Metadata
# Part Number: 1579
# Part Name: hose clamp stainless
# Version: 1
# Timestamp UTC: 20251218_033702
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular strip (main body of hose clamp)
step0 = cq.Workplane("XY").box(100, 8, 2)

# Feature 1: Cut first mounting hole (through hole perpendicular to length)
step1 = step0.faces(">Z").workplane().moveTo(-40, 0).circle(1.5).cutThruAll()

# Feature 2: Cut second mounting hole (mirrored through center)
step2 = step1.faces(">Z").workplane().moveTo(40, 0).circle(1.5).cutThruAll()

# Feature 3: Add inner edge fillet on top face (for stress relief and aesthetics)
step3 = step2.edges("|Z and <Y").fillet(0.5)

# Feature 4: Add outer edge fillet on top face
step4 = step3.edges("|Z and >Y").fillet(0.5)

# Feature 5: Create slot cutout for screw adjustment (longitudinal slot)
step5 = step4.faces(">Z").workplane().moveTo(0, 0).rect(20, 2).cutThruAll()

# Feature 6: Apply chamfer to slot ends to prevent stress concentration
step6 = step5.edges("|Y and >X").chamfer(0.3)
step7 = step6.edges("|Y and <X").chamfer(0.3)

# Feature 8: Final model with all features applied
result = step7