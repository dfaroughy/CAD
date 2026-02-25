# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
length = 100
width = 20
thickness = 10
hole_dia = 8

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create holes
step2 = step1.faces(">Z").workplane()\
    .pushPoints([(length/4, 0), (-length/4, 0)])\
    .hole(hole_dia)

# Create circular pockets on top face
step3 = step2.faces(">Z").workplane()\
    .pushPoints([(length/4, 0), (-length/4, 0)])\
    .circle(12).cutBlind(-2)

result = step3
