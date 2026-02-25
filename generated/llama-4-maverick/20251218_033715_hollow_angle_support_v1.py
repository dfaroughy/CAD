# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
length = 50
width = 30
height = 50
thickness = 5

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Step 2: Create the vertical plate
step2 = cq.Workplane("XZ").box(thickness, height, width).translate((length/2 - thickness/2, 0, thickness/2))

# Step 3: Combine the base and vertical plates
step3 = step1.union(step2)

# Step 4: Add fillets to the edges
step4 = step3.edges("|Y").fillet(2)

# Assign the final geometry to result
result = step4
