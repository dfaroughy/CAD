# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base box
step1 = cq.Workplane("XY").box(40, 20, 8)

# Step 2: Create the larger hole
step2 = step1.faces(">Z").workplane().hole(10, 8)

# Step 3: Create the smaller hole
step3 = step2.faces(">Z").workplane().center(-10, 0).hole(5, 8)

# Assign final result
result = step3
