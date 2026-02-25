# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
width = 40.0
height = 40.0
thickness = 20.0

# Create base block
step1 = cq.Workplane("XY").box(width, height, thickness)

# Create central hole
step2 = step1.faces(">Z").workplane().circle(8).cutThruAll()

# Create mounting holes
hole_offset = 15
step3 = step2.faces(">Z").workplane()\
    .pushPoints([
        (-hole_offset, -hole_offset),
        (-hole_offset, hole_offset), 
        (hole_offset, -hole_offset),
        (hole_offset, hole_offset)
    ])\
    .circle(2.5).cutThruAll()

# Create raised center section
center_width = 20.0
step4 = step3.faces(">Z").workplane()\
    .box(center_width, center_width, 20, centered=True)

# Create slot in raised section
slot_width = 5
slot_length = 12
step5 = step4.faces(">Z").workplane()\
    .slot2D(slot_length, slot_width, 0)\
    .cutThruAll()

result = step5
