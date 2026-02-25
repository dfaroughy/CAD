# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main cylindrical body
step1 = cq.Workplane("XY").circle(15).extrude(30)

# Step 2: Create the hexagonal cutout
step2 = step1.faces(">Z").workplane().polygon(6, 25.999).cutBlind(-30)

# Step 3: Create the smaller cylindrical section
step3 = step2.faces("<Z").workplane().circle(15).extrude(-10)

# Step 4: Fillet the top edge
result = step3.edges("|Z").fillet(1)
