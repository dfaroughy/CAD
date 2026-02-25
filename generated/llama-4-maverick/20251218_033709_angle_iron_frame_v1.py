# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
length = 50
width = 50
height = 50
thickness = 2

# Create the base solid
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create the vertical walls
step2 = (cq.Workplane("XY")
         .rect(length - 2 * thickness, width - 2 * thickness)
         .extrude(height - thickness))

# Create the rounded edges for the vertical walls
step3 = (step2.faces(">Z")
         .wires()
         .toPending()
         .extrude(thickness, combine=False))

# Combine the base and the walls
step4 = step1.union(step2).union(step3)

# Fillet the edges
step5 = step4.edges("|Z").fillet(2)

# Assign the final result
result = step5
