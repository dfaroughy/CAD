# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base cylinder
step1 = cq.Workplane("XY").circle(20).extrude(15)

# Step 2: Create the inner hole
step2 = step1.faces(">Z").workplane().circle(10).cutThruAll()

# Step 3: Create the notches
notch = cq.Workplane("XY").moveTo(20, 0).threePointArc((18, 2), (16, 0)).lineTo(20, 0).close().extrude(15)
step3 = step2.cut(notch.rotate((0, 0, 0), (0, 0, 1), 90))
step3 = step3.cut(notch.rotate((0, 0, 0), (0, 0, 1), 180))
step3 = step3.cut(notch.rotate((0, 0, 0), (0, 0, 1), 270))

# Assign final result
result = step3
