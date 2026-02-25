# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main rectangular prism
step1 = cq.Workplane("XY").box(60, 30, 15)

# Step 2: Create the inner cutout
step2 = step1.faces(">Z").workplane().rect(40, 15).cutBlind(-15)

# Assign final geometry to result
result = step2
