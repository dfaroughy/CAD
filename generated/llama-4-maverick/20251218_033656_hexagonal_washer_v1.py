# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
width = 19.691
height = 3.000
diameter = 17.321 / 2
distance_between_parallel_sides = 17.321

# Create the base hexagon
step1 = cq.Workplane("XY").polygon(6, distance_between_parallel_sides).extrude(height)

# Create a cylinder to cut out the center
step2 = cq.Workplane("XY").circle(diameter).extrude(height)

# Cut the cylinder from the hexagon
step3 = step1.cut(step2)

# Create two rectangular cuts on opposite sides
cut_width = 3.5
cut_depth = 3.000
cut1 = cq.Workplane("XY").rect(cut_width, cut_depth).extrude(height).translate((-width/2 + cut_width/2, 0, 0))
cut2 = cq.Workplane("XY").rect(cut_width, cut_depth).extrude(height).translate((width/2 - cut_width/2, 0, 0))

# Cut the rectangles from the hexagon
step4 = step3.cut(cut1).cut(cut2)

result = step4
