# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(80, 60, 5)

# Step 2: Cut the central rectangular hole
step2 = step1.faces(">Z").workplane().rect(40, 20).cutBlind(-5)

# Step 3: Create the holes in the corners
step3 = step2.faces(">Z").workplane().pushPoints([
    (-30, 20), (30, 20), (-30, -20), (30, -20)
]).hole(10)

# Assign final geometry to result
result = step3
