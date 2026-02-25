# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
length = 120.0
width = 40.0
thickness = 4.0
hole_dia = 5.0
hole_offset = 10.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create mounting holes
step2 = step1.faces(">Z").workplane()\
    .pushPoints([
        (-length/2 + hole_offset, width/2 - hole_offset),
        (length/2 - hole_offset, width/2 - hole_offset),
        (-length/2 + hole_offset, -width/2 + hole_offset),
        (length/2 - hole_offset, -width/2 + hole_offset)
    ])\
    .hole(hole_dia)

# Create side walls
wall_height = 10.0
step3 = step2.faces(">Z").workplane()\
    .pushPoints([(-length/2 + thickness/2, 0), (length/2 - thickness/2, 0)])\
    .rect(thickness, width).extrude(wall_height)

result = step3
