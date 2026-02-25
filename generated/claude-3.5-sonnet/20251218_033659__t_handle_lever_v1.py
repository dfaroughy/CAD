# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main body dimensions
length = 90.0
width = 30.0
height = 40.0
wall = 2.0

# Create base rectangular profile
step1 = cq.Workplane("XY").box(length, width, height)

# Hollow out the inside
step2 = step1.faces(">Z").workplane()\
    .rect(length-2*wall, width-2*wall)\
    .cutBlind(-(height-wall))

# Create U-shaped cutout in bottom
cutout_width = 10.0
cutout_height = 15.0
step3 = step2.faces("<Z").workplane()\
    .moveTo(0, 0)\
    .rect(cutout_width, width)\
    .cutBlind(cutout_height)

result = step3
