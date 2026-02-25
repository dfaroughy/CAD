# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main rectangular base
step1 = cq.Workplane("XY").box(40, 20, 51.252)

# Step 2: Create the cylindrical cutout
step2 = step1.faces(">Z").workplane().circle(10).cutBlind(-20)

# Step 3: Create the semi-circular top
step3 = step2.faces(">Z").workplane().center(0, 0).circle(10).extrude(10)

# Step 4: Create the slot in the semi-circular top
step4 = step3.faces(">Z").workplane().center(0, 0).rect(5, 20).cutBlind(-10)

# Assign final geometry to result
result = step4
