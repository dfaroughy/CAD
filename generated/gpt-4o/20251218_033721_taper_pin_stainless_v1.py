# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base cylinder
step1 = cq.Workplane("XY").circle(9.980 / 2).extrude(50.000)

# Step 2: Create the inner cylinder for hollowing
step2 = cq.Workplane("XY").circle(9.979 / 2).extrude(50.000)

# Step 3: Subtract the inner cylinder from the base cylinder
result = step1.cut(step2)
