# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main box
step1 = cq.Workplane("XY").box(100, 60, 40)

# Step 2: Create the circular cutout
step2 = step1.faces(">Z").workplane().hole(20)

# Step 3: Create the rectangular cutout
step3 = step2.faces(">Z").workplane().rect(10, 20).cutBlind(-10)

# Assign final result
result = step3
