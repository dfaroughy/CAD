# Part Metadata
# Part Number: 526
# Part Name: - wall bracket with gusset
# Version: 1
# Timestamp UTC: 20251218_033700
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 1
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create base plate of wall bracket (main extrusion)
step0 = cq.Workplane("XY").box(80, 60, 10)

# Feature 1: Extrude gusset triangle support from side face
step1 = step0.faces(">Y").workplane(centerOption="CenterOfMass").moveTo(0, 0).polyline([(0, 0), (20, 20), (-20, 20)]).close().extrude(10)

# Feature 2: Add mounting hole in base plate (cut through all)
step2 = step1.faces("<Z").workplane().moveTo(-25, 20).circle(4).cutThruAll()

# Feature 3: Add second mounting hole in base plate (cut through all)
step3 = step2.faces("<Z").workplane().moveTo(25, 20).circle(4).cutThruAll()

# Feature 4: Add fillet to sharp edges of gusset for stress relief
step4 = step3.edges("|Z").edges("<X").edges(">Y").fillet(3)

# Feature 5: Apply edge fillet to front and back edges of base plate
step5 = step4.edges("|Z").edges("#X or #Y").fillet(2)

# Feature 6: Drill hole in gusset for secondary support (cut through)
step6 = step5.faces(">Z").workplane(offset=5).moveTo(0, 10).circle(3).cutThruAll()

# Final result
result = step6