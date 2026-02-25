# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main body dimensions
length = 32.0
width = 8.0
height = 8.0

# Create base rectangular prism
step1 = cq.Workplane("XY").box(length, width, height)

# Create slot cutout
slot_width = 2.0
slot_depth = height/2
step2 = step1.faces(">Z").workplane()\
    .slot2D(length-4, slot_width, 0)\
    .extrude(-slot_depth)

# Create rounded ends
radius = width/2
step3 = step2.edges("|Z").fillet(radius)

result = step3
