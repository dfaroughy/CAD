# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main cylindrical body
step1 = cq.Workplane("XY").circle(15).extrude(20)

# Step 2: Create the hexagonal cutout
step2 = step1.faces(">Z").workplane().polygon(6, 29.999).cutBlind(-20)

# Step 3: Create the circular flange
step3 = step2.faces(">Z").workplane().circle(19.562).extrude(1.124)

# Step 4: Create the hole in the flange
step4 = step3.faces(">Z").workplane().circle(5).cutBlind(-1.124)

# Step 5: Create the side hole
step5 = step4.faces(">Y").workplane(centerOption="CenterOfBoundBox").hole(5)

# Assign final result
result = step5
