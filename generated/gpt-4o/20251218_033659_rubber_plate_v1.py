# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base rectangle
step1 = cq.Workplane("XY").rect(120, 80).extrude(5)

# Step 2: Create the two holes
step2 = step1.faces(">Z").workplane().hole(10, 5).pushPoints([(-30, 0), (30, 0)]).hole(10)

# Step 3: Create the notch at the top center
step3 = step2.faces(">Z").workplane().center(0, 40).rect(10, 5).cutBlind(-5)

# Assign final result
result = step3
