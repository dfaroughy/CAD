# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main rectangular base
step1 = cq.Workplane("XY").box(60, 8, 65)

# Step 2: Create the top cutout
step2 = step1.faces(">Z").workplane().rect(20, 8).cutBlind(-8)

# Step 3: Create the side cutouts
step3 = step2.faces(">Y").workplane().center(-20, 0).circle(4).cutBlind(-8)
step4 = step3.faces(">Y").workplane().center(40, 0).circle(4).cutBlind(-8)

# Assign final geometry to result
result = step4
