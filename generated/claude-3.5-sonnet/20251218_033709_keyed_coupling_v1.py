# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
width = 50.0
depth = 45.0
height = 50.0

# Create base block
step1 = cq.Workplane("XY").box(width, depth, height)

# Create rounded slot
slot_width = 30
slot_height = 35
slot_radius = 15

step2 = (step1
    .faces(">Z")
    .workplane()
    .slot2D(slot_width, slot_height, slot_radius)
    .cutThruAll()
)

# Create inner cutout
inner_width = 40
inner_depth = 35
inner_height = 45

step3 = (step2
    .faces(">Z")
    .workplane()
    .box(inner_width, inner_depth, inner_height, centered=True)
    .cut()
)

result = step3
