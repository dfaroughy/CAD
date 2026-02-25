# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main plate dimensions
length = 80.0
width = 60.0
thickness = 5.0
hole_dia = 5.0
edge_offset = 10.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create holes
step2 = (step1
    .faces(">Z")
    .workplane()
    .pushPoints([
        (-length/2 + edge_offset, width/2 - edge_offset),
        (length/2 - edge_offset, width/2 - edge_offset),
        (-length/2 + edge_offset, -width/2 + edge_offset),
        (length/2 - edge_offset, -width/2 + edge_offset)
    ])
    .hole(hole_dia)
)

result = step2
