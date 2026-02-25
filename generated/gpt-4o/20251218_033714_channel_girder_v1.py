# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base L shape
step1 = cq.Workplane("XY").rect(60, 50).extrude(5)

# Step 2: Cut out the inner rectangle to form the L shape
step2 = step1.faces(">Z").workplane().rect(55, 45).cutBlind(-5)

# Step 3: Add the chamfer to the outer corner
result = step2.edges("|Z").chamfer(5)
