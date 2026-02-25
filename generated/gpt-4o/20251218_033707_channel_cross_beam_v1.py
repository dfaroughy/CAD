# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the outer box
step1 = cq.Workplane("XY").box(200, 60, 10)

# Step 2: Create the inner cutout
step2 = step1.faces(">Z").workplane().rect(180, 40).cutBlind(-10)

# Assign final geometry to result
result = step2
