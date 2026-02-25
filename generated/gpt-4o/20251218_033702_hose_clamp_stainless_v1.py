# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base rectangular plate
step1 = cq.Workplane("XY").box(100, 8, 2)

# Step 2: Create the slot
step2 = step1.faces(">Z").workplane().center(0, 0).slot2D(20, 2).cutThruAll()

# Step 3: Create the holes
step3 = step2.faces(">Z").workplane().pushPoints([(-40, 0), (40, 0)]).hole(2)

# Assign final result
result = step3
