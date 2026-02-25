# Part Metadata
# Part Number: 8329
# Part Name: edge plate
# Version: 1
# Timestamp UTC: 20251218_033713
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular plate (extrusion)
step0 = cq.Workplane("XY").box(80, 60, 5)

# Feature 1: Add counterbore hole at front left corner (cut)
# Position and cut in one feature operation
step1 = step0.faces(">Z").workplane().transformed(offset=(0, 0, 0), rotate=(0, 0, 0)) \
        .moveTo(-30, 20).circle(3.5).cboreHole(6, 1.5, 2)

# Feature 2: Add counterbore hole at front right corner (cut)
# Separate feature for second hole
step2 = step1.faces(">Z").workplane().transformed(offset=(0, 0, 0), rotate=(0, 0, 0)) \
        .moveTo(30, 20).circle(3.5).cboreHole(6, 1.5, 2)

# Feature 3: Add counterbore hole at rear left corner (cut)
step3 = step2.faces(">Z").workplane().transformed(offset=(0, 0, 0), rotate=(0, 0, 0)) \
        .moveTo(-30, -20).circle(3.5).cboreHole(6, 1.5, 2)

# Feature 4: Add counterbore hole at rear right corner (cut)
step4 = step3.faces(">Z").workplane().transformed(offset=(0, 0, 0), rotate=(0, 0, 0)) \
        .moveTo(30, -20).circle(3.5).cboreHole(6, 1.5, 2)

# Feature 5: Apply fillet to all vertical edges of the plate (edge round)
step5 = step4.edges("|Z").fillet(3)

# Final result
result = step5