# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main rectangular block
step1 = cq.Workplane("XY").box(28.586, 8, 10)

# Step 2: Create the circular cutout
step2 = step1.faces(">Z").workplane().center(10, 0).hole(6)

# Step 3: Create the angled cut
step3 = step2.faces(">Z").workplane().transformed(rotate=(0, 0, 45)).rect(10, 8).cutBlind(-10)

# Assign final geometry to result
result = step3
