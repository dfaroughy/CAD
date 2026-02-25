# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
length = 42.5
width = 5.0
height = 42.5
corner_radius = 1.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, height)

# Round the corners
step2 = step1.edges("|Z").fillet(corner_radius)

# Create cutout
cutout_width = 30.0
cutout_height = 32.5
step3 = step2.faces(">Z").workplane()\
    .rect(cutout_width, cutout_height)\
    .cutThruAll()

result = step3
