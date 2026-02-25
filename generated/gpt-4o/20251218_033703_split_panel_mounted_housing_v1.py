# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main block
step1 = cq.Workplane("XY").box(80, 60, 25)

# Step 2: Cut the inner section
step2 = step1.faces(">Z").workplane().rect(60, 40).cutBlind(-20)

# Assign final result
result = step2
