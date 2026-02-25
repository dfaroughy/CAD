# Part Metadata
# Part Number: 5728
# Part Name: rounded edge prism
# Version: 1
# Timestamp UTC: 20251218_033659
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular prism (extrusion)
step0 = cq.Workplane("XY").box(60, 40, 20)

# Feature 1: Apply fillet to all vertical edges (rounding the sides)
step1 = step0.edges("|Z").fillet(5)

# Feature 2: Create top face counterbored hole (cut feature with multiple operations chained)
# Includes face selection, workplane placement, and counterbore hole cut
step2 = step1.faces(">Z").workplane().circle(3).cboreHole(8, 4, 15)

# Feature 3: Create rectangular pocket on top face (cut extrusion)
# Profile defined and cut into top face
step3 = step2.faces(">Z").workplane().rect(30, 20).cutBlind(-5)

# Feature 4: Apply chamfer to top outer perimeter edges (modify operation)
# Enhances edge detail after pocket creation
result = step3.edges("|Z").edges(">Z").chamfer(1.5)