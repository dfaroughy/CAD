# model used: anthropic/claude-3.5-sonnet
# Base plate dimensions
length = 100.0
width = 100.0
thickness = 10.0

# Hole parameters
hole_diameter = 8.0
hole_offset = 25.0
notch_width = 20.0
notch_depth = 5.0

# Construction steps
step1 = cq.Workplane("XY").box(length, width, thickness)

step2 = (step1
    .faces(">Z")
    .workplane()
    .pushPoints([
        (0, 0),  # Center hole
        (-hole_offset, -hole_offset),  # Bottom left hole  
        (hole_offset, -hole_offset)  # Bottom right hole
    ])
    .hole(hole_diameter)
)

step3 = (step2
    .faces(">Z")
    .workplane()
    .moveTo(0, -width/2)
    .rect(notch_width, notch_depth*2)
    .cutThruAll()
)

result = step3
