# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(80, 60, 5)

# Step 2: Create the central cutout
step2 = step1.faces(">Z").workplane().rect(40, 30).cutThruAll()

# Step 3: Create the four holes
step3 = step2.faces(">Z").workplane().pushPoints([
    (-30, 20), (30, 20), (-30, -20), (30, -20)
]).hole(5)

# Assign final result
result = step3
