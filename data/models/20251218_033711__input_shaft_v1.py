# Part Metadata
# Part Number: 9380
# Part Name: - input shaft
# Version: 1
# Timestamp UTC: 20251218_033711
# Generation Model: qwen.qwen3-235b-a22b-2507-v1:0
# Status: SUCCESS
# Failure Reason: None
# Debug Attempts: 2
# Debugger Model: qwen.qwen3-235b-a22b-2507-v1:0
# Geometry Fix Attempts: 0
# Geometry Fix Model: None
# Simplified Fallback: No

import cadquery as cq

# Feature 0: Create cylindrical base for input shaft (extrusion along X-axis)
step0 = cq.Workplane("YZ").circle(10).extrude(80)

# Feature 1: Add second diameter section (smaller cylinder on one end)
step1 = step0.faces("<X").workplane(centerOption="CenterOfMass").circle(8).extrude(15)

# Feature 2: Add keyway slot in the larger shaft section (cut extrusion)
step2 = step1.faces(">X").workplane(centerOption="CenterOfMass") \
          .transformed(rotate=(0, 90, 0)) \
          .rect(6, 3, centered=(True, True)).cutThruAll()

# Feature 3: Add central through hole (drilled hole along entire length)
step3 = step2.faces("<X").workplane().circle(2.5).cutThruAll()

# Feature 4: Add fillet at junction between two shaft diameters
step4 = step3.edges("|X").fillet(1.5)

# Feature 5: Add chamfer on the free end of the smaller shaft
step5 = step4.faces("<X").edges().chamfer(1)

# Feature 6: Add chamfer on the free end of the larger shaft
step6 = step5.faces(">X").edges().chamfer(1)

# Final result
result = step6