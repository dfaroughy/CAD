# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base
step1 = cq.Workplane("XY").box(50, 20, 5)

# Step 2: Create the vertical column
step2 = step1.faces(">Z").workplane().box(20, 20, 55)

# Step 3: Create the cutout rectangle
step3 = step2.faces(">Z").workplane().rect(30, 10).cutBlind(-5)

# Step 4: Create the two holes
step4 = step3.faces(">Z").workplane().pushPoints([(-10, 0), (10, 0)]).hole(5)

# Assign final result
result = step4
