# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base plate dimensions
length = 80.0
width = 60.0
thickness = 5.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness, centered=True)

# Create slots
slot_length = 20.0
slot_width = 8.0
slot_spacing = 20.0

step2 = step1.faces(">Z").workplane()\
    .rarray(slot_spacing, 1, 3, 1)\
    .slot2D(slot_length, slot_width, 0)\
    .cutThruAll()

result = step2
