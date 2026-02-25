# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Create the main cylindrical body
step1 = cq.Workplane("XY").circle(15).extrude(3)

# Create the hexagonal hole
step2 = cq.Workplane("XY").polygon(6, 6).extrude(3)

# Cut the hexagonal hole from the cylindrical body
step3 = step1.cut(step2)

# Create the rectangular prism for the top view representation
step4 = cq.Workplane("XY").box(30, 3, 30)

# The final result is the cylindrical body with the hexagonal hole
result = step3
