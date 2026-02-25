# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the hexagonal head
step1 = cq.Workplane("XY").polygon(6, 8.660).extrude(10)

# Step 2: Create the cylindrical shaft
step2 = cq.Workplane("XY").circle(5).extrude(26)

# Step 3: Combine the head and shaft
result = step1.union(step2.translate((0, 0, 10)))
