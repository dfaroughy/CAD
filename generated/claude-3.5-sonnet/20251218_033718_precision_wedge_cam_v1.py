# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
width = 60.0
height = 30.0
thickness = 15.0

# Create base plate
step1 = cq.Workplane("XY").box(width, thickness, height)

# Create vertical ribs
rib_spacing = width/4
rib_thickness = 2.0
rib_height = height-5.0

step2 = step1.faces(">Z").workplane()\
    .rarray(rib_spacing, 1, 3, 1)\
    .box(rib_thickness, thickness, rib_height, centered=(True,True,False))

result = step2
