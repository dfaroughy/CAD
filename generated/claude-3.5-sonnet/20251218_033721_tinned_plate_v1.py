# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base plate dimensions
length = 80.0
width = 60.0
thickness = 3.0

# Hole parameters
hole_diameter = 5.0
hole_margin = 10.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create holes at corners
step2 = (step1
    .faces(">Z")
    .workplane()
    .pushPoints([
        (-length/2 + hole_margin, width/2 - hole_margin),
        (length/2 - hole_margin, width/2 - hole_margin),
        (-length/2 + hole_margin, -width/2 + hole_margin),
        (length/2 - hole_margin, -width/2 + hole_margin)
    ])
    .hole(hole_diameter)
)

result = step2
