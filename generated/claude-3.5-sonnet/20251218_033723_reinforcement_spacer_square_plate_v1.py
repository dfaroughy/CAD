# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main plate dimensions
length = 80.0
width = 80.0
thickness = 10.0

# Hole parameters
hole_diameter = 5.0
hole_offset = 10.0

# Center cutout parameters
cutout_length = 40.0
cutout_width = 20.0
corner_radius = 5.0

# Construction steps
step1 = cq.Workplane("XY").box(length, width, thickness)

step2 = (step1
    .faces(">Z")
    .workplane()
    .rect(cutout_length, cutout_width, forConstruction=True)
    .vertices()
    .fillet(corner_radius)
    .cutThruAll()
)

step3 = (step2
    .faces(">Z")
    .workplane()
    .pushPoints([
        (-length/2 + hole_offset, -width/2 + hole_offset),
        (length/2 - hole_offset, -width/2 + hole_offset),
        (-length/2 + hole_offset, width/2 - hole_offset),
        (length/2 - hole_offset, width/2 - hole_offset)
    ])
    .hole(hole_diameter)
)

result = step3
