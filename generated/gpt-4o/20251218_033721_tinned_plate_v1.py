# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(80, 60, 3)

# Step 2: Create holes
step2 = step1.faces(">Z").workplane().rarray(40, 30, 2, 2).hole(5)

# Assign final result
result = step2
