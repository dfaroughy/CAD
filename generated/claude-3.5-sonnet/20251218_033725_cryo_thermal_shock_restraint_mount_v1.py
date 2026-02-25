# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
LENGTH = 60.0
WIDTH = 40.0
THICKNESS = 15.0
HOLE_DIA = 5.0
SLOT_WIDTH = 8.0
SLOT_LENGTH = 15.0

# Create base plate
step1 = cq.Workplane("XY").box(LENGTH, WIDTH, THICKNESS)

# Create mounting holes
step2 = step1.faces(">Z").workplane()\
    .pushPoints([(-20, 0), (20, 0)])\
    .hole(HOLE_DIA)

# Create center slot
step3 = step2.faces(">Z").workplane()\
    .slot2D(SLOT_LENGTH, SLOT_WIDTH, 0)\
    .cutThruAll()

result = step3
