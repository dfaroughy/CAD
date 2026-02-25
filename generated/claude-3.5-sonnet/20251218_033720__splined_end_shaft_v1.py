# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main body dimensions
length = 70.0
width = 21.751
height = 12.7

# Create base rectangular body
step1 = cq.Workplane("XY").box(length, width, height)

# Create cutout for C-shape
cutout_width = 15.1
cutout_height = 6.35
cutout_depth = width/2

step2 = step1.faces(">Y").workplane()\
    .center(length/2 - cutout_width/2, 0)\
    .box(cutout_width, cutout_depth, cutout_height, centered=(True,False,True))

# Final result
result = step2
