# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(80, 60, 5)

# Step 2: Create the holes
step2 = step1.faces(">Z").workplane().hole(10, 5).pushPoints([
    (-30, -20),
    (30, -20),
    (-30, 20),
    (30, 20)
])

# Assign final geometry to result
result = step2
