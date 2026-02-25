# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main body dimensions
length = 50.0
width = 50.0
thickness = 15.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create protruding tab
tab_length = 15.0
tab_height = 10.0
tab_thickness = thickness
tab_offset = -15.0

step2 = step1.faces(">Y").workplane()\
    .center(0, tab_offset)\
    .box(tab_length, tab_height, tab_thickness)

result = step2
