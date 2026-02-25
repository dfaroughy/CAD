# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main body dimensions
length = 150.0
width = 30.0
height = 30.0
hole_dia = 30.0

# Create base rectangular prism
step1 = cq.Workplane("XY").box(length, width, height)

# Create hole in left end
step2 = step1.faces(">X").workplane()\
    .transformed(offset=(-length/2 + 15, 0))\
    .circle(hole_dia/2)\
    .cutThru()

result = step2
