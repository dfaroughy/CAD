# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base rectangle
step1 = cq.Workplane("XY").rect(10, 7.5).extrude(50)

# Step 2: Create the slot
step2 = step1.faces(">Z").workplane().center(0, 0).slot2D(10, 7.5).cutBlind(-50)

# Assign final geometry to result
result = step2
