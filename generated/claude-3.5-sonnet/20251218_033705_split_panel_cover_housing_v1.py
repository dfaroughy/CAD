# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Dimensions
length = 125.0
width = 80.0
thickness = 10.0

# Create base profile
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create cutout
step2 = step1.faces(">Z").workplane()\
    .rect(length-2*thickness, width-2*thickness)\
    .cutThruAll()

result = step2
