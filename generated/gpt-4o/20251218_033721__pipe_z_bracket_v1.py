# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base rectangle
step1 = cq.Workplane("XY").rect(10, 7.5)

# Step 2: Extrude the rectangle to create the main body
step2 = step1.extrude(50)

# Step 3: Fillet the top edges
result = step2.edges("|Z").fillet(2.5)
