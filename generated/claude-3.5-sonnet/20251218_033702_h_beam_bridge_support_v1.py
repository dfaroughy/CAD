# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
LENGTH = 80.0
WIDTH = 10.0
HEIGHT = 30.0
HOLE_DIAMETER = 5.0
SLOT_WIDTH = 8.0
SLOT_LENGTH = 12.0

# Create base block
step1 = cq.Workplane("XY").box(LENGTH, WIDTH, HEIGHT)

# Create mounting holes
step2 = step1.faces(">Z").workplane()\
    .pushPoints([(-35,0), (35,0)])\
    .hole(HOLE_DIAMETER)

# Create slots on top
step3 = step2.faces(">Z").workplane()\
    .pushPoints([(-20,0), (0,0), (20,0)])\
    .slot2D(SLOT_LENGTH, SLOT_WIDTH, 0)\
    .cutThru()

# Create side rails
step4 = step3.faces(">Y").workplane()\
    .center(0, HEIGHT/4)\
    .rect(LENGTH, HEIGHT/2)\
    .extrude(WIDTH/4)\
    .faces("<Y").workplane()\
    .center(0, HEIGHT/4)\
    .rect(LENGTH, HEIGHT/2)\
    .extrude(WIDTH/4)

result = step4
