# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main rectangular base
step1 = cq.Workplane("XY").box(100, 60, 10)

# Step 2: Create the inner cutout
step2 = step1.faces(">Z").workplane().rect(80, 40).cutBlind(-10)

# Step 3: Create the semicircular cutout on the side
step3 = step2.faces(">Y").workplane(centerOption="CenterOfBoundBox").center(0, -20).circle(10).cutBlind(-10)

# Assign final result
result = step3
