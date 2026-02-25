# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base plate dimensions
length = 30.0
width = 3.0
thickness = 3.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create circular cutout
outer_diameter = 30.0
inner_diameter = 20.0
step2 = step1.faces(">Z").workplane()\
    .circle(outer_diameter/2)\
    .circle(inner_diameter/2)\
    .extrude(-thickness)

# Create center feature
center_width = 6.0
center_height = 4.0
step3 = step2.faces(">Z").workplane()\
    .center(0, 0)\
    .rect(center_width, center_height)\
    .extrude(-thickness/2)

result = step3
