# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base block
step1 = cq.Workplane("XY").box(40, 64, 15)

# Step 2: Create the central hole
step2 = step1.faces(">Z").workplane().hole(10)

# Step 3: Create the four corner holes
step3 = step2.faces(">Z").workplane().rect(30, 54, forConstruction=True).vertices().hole(5)

# Step 4: Create the top tab
step4 = step3.faces(">Z").workplane().center(0, 32).rect(10, 5).extrude(5)

# Assign final result
result = step4
