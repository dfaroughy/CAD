# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main rectangular base
step1 = cq.Workplane("XY").box(60, 55, 5)

# Step 2: Create the top tab
step2 = step1.faces(">Z").workplane().center(0, 27.5).rect(10, 5).extrude(5)

# Step 3: Create the hole in the top tab
step3 = step2.faces(">Z").workplane().center(0, 2.5).hole(5)

# Step 4: Create the two holes in the main base
step4 = step3.faces(">Z").workplane().center(-15, 0).hole(10)
step5 = step4.faces(">Z").workplane().center(30, 0).hole(10)

# Final result
result = step5
