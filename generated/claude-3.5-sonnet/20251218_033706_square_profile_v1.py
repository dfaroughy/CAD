# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base plate dimensions
length = 50.0
width = 50.0
thickness = 5.0

# Hole parameters
hole_diameter = 8.0
corner_hole_offset = 8.0
center_hole_diameter = 20.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create corner holes
step2 = step1.faces(">Z").workplane()\
    .pushPoints([
        (-length/2 + corner_hole_offset, width/2 - corner_hole_offset),
        (length/2 - corner_hole_offset, width/2 - corner_hole_offset),
        (-length/2 + corner_hole_offset, -width/2 + corner_hole_offset),
        (length/2 - corner_hole_offset, -width/2 + corner_hole_offset)
    ])\
    .hole(hole_diameter, thickness)

# Create center hole
step3 = step2.faces(">Z").workplane()\
    .hole(center_hole_diameter, thickness)

# Round corners
step4 = step3.edges("|Z").fillet(2.0)

result = step4
