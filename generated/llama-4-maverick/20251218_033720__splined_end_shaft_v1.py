# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
diameter = 21.751
length = 70.000

# Step 1: Create a hexagonal prism
step1 = cq.Workplane("XY").polygon(6, diameter).extrude(length)

# Step 2: Create a cylindrical hole
step2 = cq.Workplane("XY").circle(diameter/2).extrude(length)

# Step 3: Cut the hole from the prism
step3 = step1.cut(step2)

# Assign the final geometry to result
result = step3
