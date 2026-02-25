# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
width = 40
height = 60
thickness = 20
hole_diameter = 10

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(width, thickness, height)

# Step 2: Create the holes
hole1 = cq.Workplane("XY").move(-10, 0).circle(hole_diameter/2).extrude(thickness)
hole2 = cq.Workplane("XY").circle(hole_diameter/2).extrude(thickness)
hole3 = cq.Workplane("XY").move(10, 0).circle(hole_diameter/2).extrude(thickness)

# Step 3: Cut the holes from the base plate
step3 = step1.cut(hole1).cut(hole2).cut(hole3)

# Assign the final geometry to 'result'
result = step3
