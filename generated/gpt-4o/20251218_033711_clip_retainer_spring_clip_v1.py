# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base block
step1 = cq.Workplane("XY").box(20, 6, 3)

# Step 2: Cut the U-shape
step2 = step1.faces(">Z").workplane().rect(10, 3).cutBlind(-3)

# Step 3: Create the first hole
step3 = step2.faces(">Z").workplane().hole(2, depth=3, offset=(-5, 0))

# Step 4: Create the second hole
step4 = step3.faces(">Z").workplane().hole(2, depth=3, offset=(5, 0))

# Assign final geometry to result
result = step4
