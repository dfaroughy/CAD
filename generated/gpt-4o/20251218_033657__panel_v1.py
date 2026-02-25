# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(120, 60, 5)

# Step 2: Create the central hole
step2 = step1.faces(">Z").workplane().hole(20)

# Step 3: Create the two smaller holes
step3 = step2.faces(">Z").workplane().pushPoints([(-40, 0), (40, 0)]).hole(10)

# Assign final geometry to result
result = step3
