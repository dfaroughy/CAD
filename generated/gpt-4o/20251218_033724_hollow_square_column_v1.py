# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the outer box
step1 = cq.Workplane("XY").box(50, 50, 100)

# Step 2: Hollow out the box to create the outer shell
step2 = step1.faces(">Z").workplane().rect(46, 46).cutBlind(-100)

# Step 3: Create the inner cutout
step3 = step2.faces(">Z").workplane().rect(30, 30).cutBlind(-100)

# Step 4: Create the bottom notch
step4 = step3.faces("<Z").workplane().center(0, -20).rect(10, 10).cutBlind(5)

# Assign final geometry to result
result = step4
