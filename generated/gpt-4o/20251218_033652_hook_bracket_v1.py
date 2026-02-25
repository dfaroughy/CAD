# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main rectangular base
step1 = cq.Workplane("XY").box(60, 50, 20)

# Step 2: Create the top rectangular feature
step2 = cq.Workplane("XY").workplane(offset=20).center(0, 0).box(20, 10, 20)

# Step 3: Combine the two parts
result = step1.union(step2)
