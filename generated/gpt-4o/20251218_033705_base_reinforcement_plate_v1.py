# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(120, 80, 8)

# Step 2: Create the central hole
step2 = step1.faces(">Z").workplane().hole(20)

# Step 3: Create the corner holes
step3 = step2.faces(">Z").workplane().pushPoints([
    (-50, -30), (50, -30), (-50, 30), (50, 30)
]).hole(10)

# Assign final result
result = step3
