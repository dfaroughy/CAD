# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base rectangle
step1 = cq.Workplane("XY").box(80, 60, 5)

# Step 2: Cut the large circle
step2 = step1.faces(">Z").workplane().hole(20)

# Step 3: Cut the small circle
step3 = step2.faces(">Z").workplane().center(30, -20).hole(10)

# Step 4: Create the notch
step4 = step3.faces(">Z").workplane().center(40, -30).rect(5, 5).cutBlind(-5)

# Assign final geometry to result
result = step4
