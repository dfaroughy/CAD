# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main rectangular base
step1 = cq.Workplane("XY").box(125, 80, 10)

# Step 2: Create the inner cutout
step2 = step1.faces(">Z").workplane().rect(115, 70).cutBlind(-10)

# Step 3: Create the notch on the top edge
step3 = step2.faces(">Z").workplane().center(0, 40).rect(10, 5).cutBlind(-10)

# Step 4: Create the side protrusion
step4 = step3.faces(">Y").workplane(centerOption="CenterOfBoundBox").center(0, 0).rect(10, 5).extrude(5)

# Assign final result
result = step4
