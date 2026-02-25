# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main dimensions
length = 80.0
width = 60.0
thickness = 2.0
hole_dia = 20.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create centered hole
step2 = step1.faces(">Z").workplane()\
    .circle(hole_dia/2)\
    .cutThrough()

result = step2
