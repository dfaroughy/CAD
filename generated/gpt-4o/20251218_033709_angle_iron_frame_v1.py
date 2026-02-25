# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base square plate
step1 = cq.Workplane("XY").box(50, 50, 5)

# Step 2: Create the L-shaped cutout
step2 = step1.faces(">Z").workplane().rect(45, 45).cutBlind(-5)

# Step 3: Fillet the inner edges of the L-shape
step3 = step2.edges("|Z").fillet(2.5)

# Assign final result
result = step3
