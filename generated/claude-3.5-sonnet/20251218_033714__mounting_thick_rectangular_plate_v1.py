# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base plate dimensions
length = 120.0
width = 25.0
thickness = 8.0

# Hole parameters
hole_diameter = 6.0
edge_margin = 7.5
center_hole_y = width/2

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create mounting holes
step2 = step1.faces(">Z").workplane()\
    .pushPoints([(length/4, center_hole_y),
                (-length/4, center_hole_y),
                (length/4, -center_hole_y),
                (-length/4, -center_hole_y)])\
    .hole(hole_diameter)

# Create center hole
step3 = step2.faces(">Z").workplane()\
    .hole(hole_diameter)

result = step3
