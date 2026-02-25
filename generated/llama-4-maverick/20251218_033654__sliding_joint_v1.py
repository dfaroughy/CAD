# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
length = 60
width = 30
height = 15

# Step 1: Create the outer rectangle
step1 = cq.Workplane("XY").box(length, width, height)

# Step 2: Create the inner pocket rectangle
inner_length = length - 10
inner_width = width - 10
step2 = cq.Workplane("XY").box(inner_length, inner_width, height)

# Step 3: Cut the inner pocket from the outer rectangle
step3 = step1.cut(step2.translate((0, 0, height/2)))

# Step 4: Add fillets to the edges
step4 = step3.edges("|Z").fillet(2)

# Assign the final geometry to result
result = step4
