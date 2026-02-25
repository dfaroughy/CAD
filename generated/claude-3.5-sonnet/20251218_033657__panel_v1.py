# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main L-bracket dimensions
length = 120.0
height = 60.0
thickness = 5.0

# Create base L shape
step1 = cq.Workplane("XY").box(length, thickness, height, centered=(True, True, False))
step2 = step1.faces(">Y").workplane().box(thickness, height, height, centered=(False, True, False))

# Move to origin
step3 = step2.translate((-length/2, -thickness/2, 0))

# Add holes
hole_diameter = 5.0
hole_edge_distance = 15.0

step4 = step3.faces(">Z").workplane() \
    .pushPoints([
        (hole_edge_distance, 0),
        (length - hole_edge_distance, 0)
    ]) \
    .hole(hole_diameter)

result = step4
