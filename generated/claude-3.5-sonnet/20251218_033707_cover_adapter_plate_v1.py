# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base plate dimensions
length = 80.0
width = 60.0
thickness = 8.0

# Hole parameters
hole_diameter = 5.0
hole_spacing_x = 60.0
hole_spacing_y = 40.0
center_hole_diameter = 30.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create mounting holes
step2 = step1.faces(">Z").workplane()\
    .rect(hole_spacing_x, hole_spacing_y, forConstruction=True)\
    .vertices()\
    .hole(hole_diameter, thickness)

# Create center hole
step3 = step2.faces(">Z").workplane()\
    .hole(center_hole_diameter, thickness)

result = step3
