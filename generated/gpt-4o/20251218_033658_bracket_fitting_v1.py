# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base box
step1 = cq.Workplane("XY").box(60, 40, 15)

# Step 2: Apply fillet to the top edges
step2 = step1.edges("|Z").fillet(5)

# Assign final geometry to result
result = step2
