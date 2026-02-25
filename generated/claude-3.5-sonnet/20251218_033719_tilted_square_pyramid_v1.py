# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
width = 50.0
height = 50.0
thickness = 2.0

# Create base plate
step1 = cq.Workplane("XY").box(width, height, thickness)

# Create vertical wall
step2 = step1.faces(">Z").workplane()\
    .moveTo(-width/2 + thickness/2, 0)\
    .rect(thickness, height)\
    .extrude(27.0)

# Create horizontal shelf
step3 = step2.faces(">Z").workplane()\
    .moveTo(5, 0)\
    .rect(15, thickness)\
    .extrude(-thickness)

# Create small vertical support
step4 = step3.faces(">Z").workplane()\
    .moveTo(10, 5)\
    .rect(thickness, 10)\
    .extrude(-8)

result = step4
