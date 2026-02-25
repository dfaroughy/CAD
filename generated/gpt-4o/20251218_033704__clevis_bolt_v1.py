# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main rectangular base
step1 = cq.Workplane("XY").box(25, 15, 46)

# Step 2: Create the hexagonal cutout
step2 = step1.faces(">Z").workplane().polygon(6, 10).cutBlind(-15)

# Step 3: Create the cylindrical cutout
step3 = step2.faces(">Z").workplane().circle(5).cutBlind(-15)

# Assign final result
result = step3
