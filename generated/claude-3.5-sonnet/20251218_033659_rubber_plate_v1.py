# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main box dimensions
length = 120.0
width = 80.0
thickness = 5.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create walls
wall_height = 5.0
step2 = step1.faces(">Z").workplane().rect(length, width).extrude(wall_height)

# Cut out inner cavity
inner_length = length - 2*thickness
inner_width = width - 2*thickness
step3 = step2.faces(">Z").workplane().rect(inner_length, inner_width).cutThruAll()

# Add notch in top edge
notch_width = 20.0
notch_depth = 5.0
step4 = step3.faces(">Y").workplane()\
    .center(0, wall_height/2)\
    .rect(notch_width, notch_depth)\
    .cutThruAll()

# Add mounting holes
hole_diameter = 8.0
hole_spacing_x = 80.0
step5 = step4.faces(">Z").workplane()\
    .pushPoints([(-hole_spacing_x/2, 0), (hole_spacing_x/2, 0)])\
    .hole(hole_diameter)

result = step5
