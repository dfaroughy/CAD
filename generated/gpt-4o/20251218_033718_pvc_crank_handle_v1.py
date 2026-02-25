# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main cylinder
step1 = cq.Workplane("XY").circle(15).extrude(150)

# Step 2: Create the inner cylinder
step2 = cq.Workplane("XY").circle(14.9995).extrude(150)

# Step 3: Subtract the inner cylinder from the main cylinder
result = step1.cut(step2)
