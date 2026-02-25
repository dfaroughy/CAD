# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base box
step1 = cq.Workplane("XY").box(60, 60, 8)

# Step 2: Cut the top left notch
step2 = step1.faces(">Z").workplane().rect(20, 20).cutBlind(-8)

# Step 3: Cut the bottom right notch
step3 = step2.faces(">Z").workplane().rect(20, 30).center(20, -15).cutBlind(-8)

# Step 4: Cut the middle notch
step4 = step3.faces(">Z").workplane().rect(20, 10).center(-20, 15).cutBlind(-8)

# Assign final geometry to result
result = step4
