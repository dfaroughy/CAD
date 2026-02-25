# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create a cylinder
step1 = cq.Workplane("XY").circle(25).extrude(50)

# Step 2: Create a wedge shape to cut
step2 = cq.Workplane("XY").moveTo(-25, 0).lineTo(25, 0).lineTo(25, 50).lineTo(-15, 50).close().extrude(50)

# Step 3: Cut the wedge from the cylinder
result = step1.cut(step2)
