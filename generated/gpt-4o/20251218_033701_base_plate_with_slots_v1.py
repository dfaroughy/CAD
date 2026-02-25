# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base rectangle
step1 = cq.Workplane("XY").box(80, 60, 5)

# Step 2: Create the circular hole
step2 = step1.faces(">Z").workplane().hole(10, 5)

# Step 3: Create the first slot
step3 = step2.faces(">Z").workplane().slot2D(30, 10).cutThruAll()

# Step 4: Create the second slot
step4 = step3.faces(">Z").workplane().center(30, 0).slot2D(30, 10).cutThruAll()

# Assign final result
result = step4
