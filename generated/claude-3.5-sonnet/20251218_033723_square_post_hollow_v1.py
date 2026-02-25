# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
width = 100.0
height = 50.0
thickness = 50.0
slot_width = 50.0
slot_depth = 25.0

# Create base block
step1 = cq.Workplane("XY").box(width, height, thickness)

# Create slot
step2 = (step1
         .faces(">Z")
         .workplane()
         .slot2D(slot_width, slot_depth, 0)
         .cutThruAll()
)

result = step2
