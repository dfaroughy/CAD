# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
length = 60.0
width = 40.0
height = 20.0
wall = 2.0

# Create base box with rounded corners
step1 = cq.Workplane("XY").box(length, width, height)

# Create inner void
step2 = step1.faces(">Z").workplane()\
    .box(length-2*wall, width-2*wall, height-wall)\
    .translate((0,0,-wall/2))

# Subtract inner void from base
step3 = step1.cut(step2)

# Add rounded corners
result = step3.edges("|Z").fillet(3.0)
