# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main box dimensions
length = 40.0
width = 20.0
height = 8.0
wall_thickness = 1.0

# Create outer box
step1 = cq.Workplane("XY").box(length, width, height)

# Create inner cavity by subtracting smaller box
step2 = step1.faces(">Z").workplane()\
    .box(length-2*wall_thickness, width-2*wall_thickness, height-wall_thickness)\
    .translate((0,0,-wall_thickness/2))

# Create main circular cutout
step3 = step2.faces(">Z").workplane()\
    .circle(7.0)\
    .cutThrough()

# Create smaller circular cutout
step4 = step3.faces(">Z").workplane()\
    .circle(2.5)\
    .translate((-12,0,0))\
    .cutThrough()

result = step4
