# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base plate dimensions
length = 120.0
width = 80.0
thickness = 5.0

# Hole parameters
hole_dia = 8.0
hole_margin = 20.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create holes pattern
hole_centers = [
    (-length/4, width/4),
    (length/4, width/4), 
    (-length/4, -width/4),
    (length/4, -width/4),
    (0, 0)
]

# Add mounting holes
step2 = step1.faces(">Z").workplane()\
    .pushPoints(hole_centers)\
    .hole(hole_dia)

# Create bent flange
step3 = step2.faces(">Y").workplane()\
    .transformed(rotate=(90, 0, 0))\
    .rect(length, thickness)\
    .extrude(width/2)

result = step3
