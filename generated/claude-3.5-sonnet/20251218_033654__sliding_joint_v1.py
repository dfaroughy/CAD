# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
length = 60.0
width = 30.0
thickness = 15.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create cutout dimensions
cutout_length = 20.0
cutout_width = 15.0
cutout_offset = 10.0

# Create cutout
step2 = step1.faces(">Z").workplane()\
    .center(cutout_offset, 0)\
    .box(cutout_length, cutout_width, thickness, centered=(True,True,False))\
    .cut()

result = step2
