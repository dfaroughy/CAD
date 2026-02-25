# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main rectangular base
step1 = cq.Workplane("XY").box(40, 75, 5)

# Step 2: Create the top tab with a hole
step2 = step1.faces(">Y").workplane().center(0, 37.5).rect(10, 5).extrude(5)

# Step 3: Create the hole in the tab
step3 = step2.faces(">Y").workplane().center(0, 2.5).hole(5)

# Step 4: Create the rectangular cutout
step4 = step3.faces("<Z").workplane().center(0, -20).rect(20, 10).cutBlind(-5)

# Assign final geometry to result
result = step4
