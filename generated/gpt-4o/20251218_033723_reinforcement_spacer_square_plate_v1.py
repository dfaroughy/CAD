# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(80, 80, 10)

# Step 2: Create the central square cutout
step2 = step1.faces(">Z").workplane().rect(40, 40).cutBlind(-10)

# Step 3: Create the four corner holes
step3 = step2.faces(">Z").workplane().pushPoints([
    (-30, -30), (30, -30), (-30, 30), (30, 30)
]).hole(10)

# Assign final geometry to result
result = step3
