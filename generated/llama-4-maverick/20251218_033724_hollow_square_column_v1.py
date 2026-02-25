# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
length = 100
width = 50
height = 50
thickness = 5

# Step 1: Create the base rectangle
step1 = cq.Workplane("XY").rect(length, width).extrude(height)

# Step 2: Create the inner cavity
inner_length = length - 2 * thickness
inner_width = width - 2 * thickness
inner_height = height
step2 = cq.Workplane("XY").rect(inner_length, inner_width).extrude(inner_height).translate((0, 0, thickness))

# Step 3: Cut out the inner cavity from the base
step3 = step1.cut(step2)

# Step 4: Add the bottom thickness
step4 = step3.faces(">Z").workplane().rect(length, width).extrude(-thickness)

# Step 5: Create the final part by combining the steps
result = step4
