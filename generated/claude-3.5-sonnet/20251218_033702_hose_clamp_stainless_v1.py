# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
length = 100.0
width = 8.0
thickness = 2.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create holes
hole_dia = 2.0
hole_spacing = 90.0

step2 = step1.faces(">Z").workplane()\
    .pushPoints([(-hole_spacing/2, 0), (hole_spacing/2, 0)])\
    .hole(hole_dia)

# Create center slot
slot_width = 2.0
slot_length = 20.0

step3 = step2.faces(">Z").workplane()\
    .slot2D(slot_length, slot_width, 0)\
    .cutThruAll()

result = step3
