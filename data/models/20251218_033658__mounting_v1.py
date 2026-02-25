# Part Metadata
# Part Number: 8848
# Part Name: - mounting
# Version: 1
# Timestamp UTC: 20251218_033658
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 0
# Debugger Model: None
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base rectangular extrusion for mounting plate
step0 = cq.Workplane("XY").box(60, 40, 8)

# Feature 1: Cut central rectangular hole through the thickness
step1 = step0.faces(">Z").workplane().rect(30, 20).cutThruAll()

# Feature 2: Drill first through hole near front-left corner
step2 = step1.faces(">Z").workplane().moveTo(15, 15).circle(3.5).cutThruAll()

# Feature 3: Drill second through hole near front-right corner
step3 = step2.faces(">Z").workplane().moveTo(-15, 15).circle(3.5).cutThruAll()

# Feature 4: Drill third through hole near rear-left corner
step4 = step3.faces(">Z").workplane().moveTo(15, -15).circle(3.5).cutThruAll()

# Feature 5: Drill fourth through hole near rear-right corner
step5 = step4.faces(">Z").workplane().moveTo(-15, -15).circle(3.5).cutThruAll()

# Feature 6: Apply fillet to all vertical edges of the base (around perimeter)
step6 = step5.edges("|Z").fillet(3)

# Feature 7: Apply smaller fillet to the inner edge of the central rectangular cut
step7 = step6.edges(cq.selectors.NearestToPointSelector((0, 0, 0))).fillet(2)

# Final result
result = step7