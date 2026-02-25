# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
length = 200.0
width = 40.0
thickness = 60.0

# Create base box
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create cutouts for grip
cutout_width = 10
cutout_depth = 5
cutout_offset = 40

step2 = step1.faces(">Z").workplane()\
    .center(-cutout_offset, 0).rect(cutout_width, width).cutBlind(-cutout_depth)\
    .center(2*cutout_offset, 0).rect(cutout_width, width).cutBlind(-cutout_depth)

result = step2
