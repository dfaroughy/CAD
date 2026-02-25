# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main box dimensions
length = 100.0
width = 60.0
height = 40.0
thickness = 2.0

# Create outer box
step1 = cq.Workplane("XY").box(length, width, height)

# Create inner void
step2 = step1.faces(">Z").workplane()\
    .box(length-2*thickness, width-2*thickness, height-thickness)\
    .translate((0,0,-thickness/2))

# Subtract inner void
step3 = step1.cut(step2)

# Add hole in top
hole_dia = 8.0
step4 = step3.faces(">Z").workplane()\
    .hole(hole_dia)

result = step4
