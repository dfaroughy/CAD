# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create a base square
step1 = cq.Workplane("XY").box(50, 50, 50)

# Step 2: Apply a chamfer to all edges
result = step1.edges().chamfer(5)
