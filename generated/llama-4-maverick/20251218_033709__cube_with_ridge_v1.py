# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
length = 50.0
width = 50.0
height = 15.0
notch_width = 5.0  # Assuming a notch width of 5.0 based on the drawing
notch_height = 5.0  # Assuming a notch height of 5.0 based on the drawing

# Step 1: Create the base rectangular solid
step1 = cq.Workplane("XY").box(length, width, height)

# Step 2: Create a rectangular solid for the notch
step2 = cq.Workplane("XY").box(notch_width, notch_height, height).translate((length/2 - notch_width/2, -width/2, 0))

# Step 3: Cut the notch from both sides
step3 = step1.cut(step2).cut(step2.rotate((0,0,0), (0,0,1), 180))

# Step 4: Create a rectangular solid for the fillet
step4 = step3.edges("|Z").fillet(5.0)

# Assign the final geometry to result
result = step4
