# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
length = 50.0
width = 20.0
height = 55.0
base_height = 5.0

# Create base block
step1 = cq.Workplane("XY").box(length, width, base_height)

# Create vertical post
post_width = 8.0
post_length = 8.0
step2 = step1.faces(">Z").workplane()\
    .center(0, 0)\
    .box(post_width, post_length, height-base_height)

# Add rounded top piece
top_width = 20.0
top_length = 20.0
top_height = 5.0
radius = 2.0

step3 = step2.faces(">Z").workplane()\
    .center(0, 0)\
    .box(top_width, top_length, top_height)\
    .edges("|Z").fillet(radius)

result = step3
