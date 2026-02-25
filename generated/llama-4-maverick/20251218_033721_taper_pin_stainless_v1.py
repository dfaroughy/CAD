# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
outer_diameter = 9.980
inner_diameter = 9.079
height = 50.000

# Step 1: Create the outer cylinder
step1 = cq.Workplane("XY").circle(outer_diameter/2).extrude(height)

# Step 2: Create the inner cylinder
step2 = cq.Workplane("XY").circle(inner_diameter/2).extrude(height)

# Step 3: Subtract the inner cylinder from the outer cylinder
result = step1 - step2

result
