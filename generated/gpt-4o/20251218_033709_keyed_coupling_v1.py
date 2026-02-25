# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main outer cylinder
step1 = cq.Workplane("XY").circle(25).extrude(45)

# Step 2: Create the inner cylinder cutout
step2 = step1.faces(">Z").workplane().circle(15).cutBlind(-45)

# Step 3: Create the smaller outer cylinder
step3 = step2.faces(">Z").workplane().circle(22.5).extrude(5)

# Step 4: Create the smaller inner cylinder cutout
step4 = step3.faces(">Z").workplane().circle(12.5).cutBlind(-5)

# Assign final geometry to result
result = step4
