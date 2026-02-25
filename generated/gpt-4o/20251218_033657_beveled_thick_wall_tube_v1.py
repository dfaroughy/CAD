# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base cylinder
step1 = cq.Workplane("XY").circle(25).extrude(50)

# Step 2: Create the inner cut cylinder
step2 = cq.Workplane("XY").circle(20).extrude(50)

# Step 3: Subtract the inner cylinder from the base cylinder
step3 = step1.cut(step2)

# Step 4: Apply chamfer to the edges
result = step3.edges("|Z").chamfer(2)
