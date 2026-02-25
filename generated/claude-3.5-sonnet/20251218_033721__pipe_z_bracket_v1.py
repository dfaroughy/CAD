# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
width = 10.0
height = 50.0
thickness = 7.0
notch_depth = 2.0
notch_height = 2.0

# Create base extrusion
step1 = cq.Workplane("XY").box(width, thickness, height)

# Create notch cutout
step2 = (step1
         .faces(">Z")
         .workplane()
         .rect(notch_depth*2, thickness)
         .cutBlind(-notch_height)
)

result = step2
