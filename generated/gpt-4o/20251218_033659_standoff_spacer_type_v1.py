# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main cylinder
step1 = cq.Workplane("XY").circle(6).extrude(10)

# Step 2: Create the inner hole
step2 = step1.faces(">Z").workplane().circle(3.5).cutThruAll()

# Step 3: Add chamfers to the edges
result = step2.edges("|Z").chamfer(0.7)
