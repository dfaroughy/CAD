# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base box
step1 = cq.Workplane("XY").box(60, 40, 20)

# Step 2: Apply fillet to the edges
result = step1.edges("|Z").fillet(10)
