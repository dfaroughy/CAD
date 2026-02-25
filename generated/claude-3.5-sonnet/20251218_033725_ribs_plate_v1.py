# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main body dimensions
length = 120.0
width = 97.5
thickness = 18.5
hole_dia = 8.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Add mounting holes
step2 = step1.faces(">Z").workplane()\
    .pushPoints([(-30, 0), (30, 0)])\
    .hole(hole_dia)

# Add top protrusion
top_width = 30.0
top_height = 20.0
step3 = step2.faces(">Z").workplane()\
    .center(0, width/2 - top_height/2)\
    .box(top_width, top_height, thickness/2)

result = step3
