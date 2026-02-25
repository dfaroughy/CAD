# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base rectangle
step1 = cq.Workplane("XY").rect(60, 50).extrude(5)

# Step 2: Create the cutout on the top and bottom edges
step2 = step1.faces(">Z").workplane().center(0, 25).rect(10, 5).cutBlind(-5)
step3 = step2.faces(">Z").workplane().center(0, -25).rect(10, 5).cutBlind(-5)

# Step 3: Create the central hole
step4 = step3.faces(">Z").workplane().center(0, 0).circle(5).cutBlind(-5)

# Assign final geometry to result
result = step4
