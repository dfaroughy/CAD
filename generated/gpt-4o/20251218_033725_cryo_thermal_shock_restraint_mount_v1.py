# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main box
step1 = cq.Workplane("XY").box(60, 40, 15)

# Step 2: Create the central hole
step2 = step1.faces(">Z").workplane().hole(10)

# Step 3: Create the slot
step3 = step2.faces(">Z").workplane().slot2D(30, 10).cutThruAll()

# Step 4: Create the two side holes
step4 = step3.faces(">Z").workplane().pushPoints([(-20, 0), (20, 0)]).hole(10)

# Assign final result
result = step4
