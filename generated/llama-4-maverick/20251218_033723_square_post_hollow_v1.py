# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
length = 100
width = 50
height = 50
wall_thickness = 5

# Step 1: Create the outer box
step1 = cq.Workplane("XY").box(length, width, height)

# Step 2: Create the inner box
inner_length = length - 2 * wall_thickness
inner_width = width - 2 * wall_thickness
inner_height = height
step2 = cq.Workplane("XY").box(inner_length, inner_width, inner_height).translate((0, 0, wall_thickness))

# Step 3: Cut out the inner box from the outer box
step3 = step1.cut(step2)

# Step 4: Create the cavity
cavity_length = inner_length - 2 * wall_thickness
cavity_width = inner_width - 2 * wall_thickness
cavity_height = height - wall_thickness
step4 = cq.Workplane("XY").box(cavity_length, cavity_width, cavity_height).translate((0, 0, wall_thickness))

# Step 5: Cut out the cavity from the outer box
step5 = step3.cut(step4)

# Assign the final geometry to 'result'
result = step5
