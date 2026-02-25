# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main cylinder
step1 = cq.Workplane("XY").circle(6).extrude(10)

# Step 2: Create the inner cut cylinder
step2 = cq.Workplane("XY").circle(5.9995).extrude(10)

# Step 3: Subtract the inner cylinder from the main cylinder
step3 = step1.cut(step2)

# Step 4: Fillet the edges
result = step3.edges("|Z").fillet(1)
