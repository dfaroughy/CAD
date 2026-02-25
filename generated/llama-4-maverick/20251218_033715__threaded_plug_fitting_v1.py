# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
width = 30
height = 30
hex_size = 15

# Step 1: Create the base cylinder
step1 = cq.Workplane("XY").circle(width/2).extrude(height)

# Step 2: Create the hexagonal hole
step2 = cq.Workplane("XY").polygon(6, hex_size).extrude(height)

# Step 3: Create the outer shell
step3 = step1.faces(">Z").workplane().circle(width/2 - 2).extrude(-height, combine=False)

# Step 4: Create the final object by cutting the hexagonal hole from the base cylinder
step4 = step1.cut(step2)

# Step 5: Create the final object by cutting the outer shell from the base cylinder and then filleting the edges
result = step4.edges("|Z").fillet(1)
