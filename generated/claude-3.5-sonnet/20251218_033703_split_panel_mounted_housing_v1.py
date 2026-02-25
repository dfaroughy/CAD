# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main dimensions
length = 80.0
width = 60.0
height = 25.0
wall_thickness = 2.0

# Create outer box
step1 = cq.Workplane("XY").box(length, width, height)

# Create inner cavity by subtracting smaller box
step2 = step1.faces(">Z").workplane()\
    .box(length-2*wall_thickness, width-2*wall_thickness, height-wall_thickness)\
    .translate((0,0,-wall_thickness/2))

# Cut out the cavity
step3 = step1.cut(step2)

result = step3
