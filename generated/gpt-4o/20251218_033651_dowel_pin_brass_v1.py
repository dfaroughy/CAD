# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base cylinder
step1 = cq.Workplane("XY").circle(3).extrude(20)

# Step 2: Create the inner cylinder for hollowing
step2 = cq.Workplane("XY").circle(2.5).extrude(20)

# Step 3: Subtract the inner cylinder from the base cylinder
result = step1.cut(step2)
