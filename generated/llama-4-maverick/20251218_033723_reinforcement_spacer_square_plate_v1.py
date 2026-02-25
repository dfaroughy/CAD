# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
length = 80
width = 80
thickness = 10
hole_diameter = 8
pocket_length = 40
pocket_width = 20

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Step 2: Create the holes
hole_positions = [(length/4, width/4), (length*3/4, width/4), (length/4, width*3/4), (length*3/4, width*3/4)]
step2 = step1.faces(">Z").workplane().pushPoints(hole_positions).hole(hole_diameter, thickness)

# Step 3: Create the pocket
step3 = step2.faces(">Z").workplane().rect(pocket_length, pocket_width).cutBlind(-thickness/2)

# Assign the final geometry to result
result = step3
