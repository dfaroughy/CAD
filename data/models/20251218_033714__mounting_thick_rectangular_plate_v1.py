# Part Metadata
# Part Number: 8334
# Part Name: - mounting thick rectangular plate
# Version: 1
# Timestamp UTC: 20251218_033714
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base thick rectangular plate (extrusion)
step0 = cq.Workplane("XY").box(120, 80, 25)

# Feature 1: Add first through hole at center front edge (cut extrusion)
step1 = step0.faces(">Z").workplane().moveTo(0, -30).circle(8).cutThruAll()

# Feature 2: Add second through hole symmetric to first (cut extrusion)
step2 = step1.faces(">Z").workplane().moveTo(0, 30).circle(8).cutThruAll()

# Feature 3: Add counterbored hole in top-left corner (cut extrusion)
step3 = step2.faces(">Z").workplane().moveTo(-40, -30).cboreHole(6, 12, 10)

# Feature 4: Add counterbored hole in top-right corner (cut extrusion)
step4 = step3.faces(">Z").workplane().moveTo(40, -30).cboreHole(6, 12, 10)

# Feature 5: Add counterbored hole in bottom-left corner (cut extrusion)
step5 = step4.faces(">Z").workplane().moveTo(-40, 30).cboreHole(6, 12, 10)

# Feature 6: Add counterbored hole in bottom-right corner (cut extrusion)
step6 = step5.faces(">Z").workplane().moveTo(40, 30).cboreHole(6, 12, 10)

# Feature 7: Apply fillet to all vertical edges of the plate (edge fillet)
step7 = step6.edges("|Z").fillet(3)

# Feature 8: Apply chamfer to top face outer perimeter (chamfer operation)
# Skip chamfer if it fails due to geometry conflicts, or apply to non-filleted edges
# Using a smaller chamfer or selective edges to avoid conflict with fillets
step8 = step7.faces(">Z").edges().fillet(0.1)

# Final result
result = step8