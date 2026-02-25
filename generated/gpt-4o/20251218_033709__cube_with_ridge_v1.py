# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main box
step1 = cq.Workplane("XY").box(50, 50, 15)

# Step 2: Create the cutout
step2 = step1.faces(">Z").workplane().rect(50, 5).cutBlind(-15)

# Step 3: Create the protrusion
step3 = step2.faces(">Y").workplane(centerOption="CenterOfBoundBox").rect(5, 15).extrude(15)

# Assign final result
result = step3
