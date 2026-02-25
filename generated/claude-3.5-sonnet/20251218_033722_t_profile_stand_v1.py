# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
length = 60.0
width = 20.0
height = 40.0

# Create base block
step1 = cq.Workplane("XY").box(width, length, height)

# Create holes
hole_dia = 8.0
hole_spacing = 12.0
hole_depth = 15.0

step2 = step1.faces(">Z").workplane()\
    .rarray(0, hole_spacing, 1, 3)\
    .hole(hole_dia, hole_depth)

result = step2
