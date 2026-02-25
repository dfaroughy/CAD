# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base plate dimensions
LENGTH = 100.0
WIDTH = 100.0
THICKNESS = 20.0

# Create base plate
step1 = cq.Workplane("XY").box(LENGTH, WIDTH, THICKNESS)

# Create central circular cutout
step2 = step1.faces(">Z").workplane()\
    .circle(30)\
    .cutThrough()

# Create corner mounting holes
step3 = step2.faces(">Z").workplane()\
    .pushPoints([
        (-40, 40), (40, 40),
        (-40, -40), (40, -40)
    ])\
    .circle(5)\
    .cutThrough()

# Create side slots
step4 = step3.faces(">Z").workplane()\
    .pushPoints([
        (-45, 0), (45, 0),
        (0, -45), (0, 45)
    ])\
    .slot2D(20, 8, 90)\
    .cutThrough()

result = step4
