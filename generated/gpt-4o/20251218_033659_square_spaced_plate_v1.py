# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(100, 100, 10)

# Step 2: Create the holes
step2 = step1.faces(">Z").workplane().hole(10, 10)
step3 = step2.faces(">Z").workplane().center(-30, 30).hole(10, 10)
step4 = step3.faces(">Z").workplane().center(60, 0).hole(10, 10)
step5 = step4.faces(">Z").workplane().center(-30, -60).hole(10, 10)

# Step 3: Create the notch
step6 = step5.faces(">Z").workplane().center(0, -50).rect(10, 5).cutBlind(-1)

# Final result
result = step6
