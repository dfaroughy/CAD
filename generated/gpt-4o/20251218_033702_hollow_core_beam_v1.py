# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base rectangle
step1 = cq.Workplane("XY").rect(200, 60).extrude(10)

# Step 2: Create the inner cutout
step2 = step1.faces(">Z").workplane().rect(180, 40).cutBlind(-10)

# Step 3: Create the central circular cutout
step3 = step2.faces(">Z").workplane().circle(10).cutBlind(-10)

# Step 4: Create the slot on the right side
step4 = step3.faces(">Z").workplane().center(50, 0).slot2D(40, 10).cutBlind(-10)

# Assign final result
result = step4
