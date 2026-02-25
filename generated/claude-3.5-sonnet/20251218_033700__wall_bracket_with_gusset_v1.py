# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
width = 80.0
height = 70.0
thickness = 25.0

# Create base plate
step1 = cq.Workplane("XY").box(width, height, thickness)

# Add mounting holes
step2 = step1.faces(">Z").workplane()\
    .pushPoints([(-20,0), (20,0)])\
    .hole(diameter=8)

# Create top section
step3 = step2.faces(">Z").workplane()\
    .center(0, height/2)\
    .rect(width, thickness)\
    .extrude(thickness)

# Add triangular supports
points = [
    (-width/4, 0),
    (0, height/4), 
    (width/4, 0)
]

step4 = step3.faces(">Z").workplane()\
    .center(0, height/4)\
    .polyline(points)\
    .close()\
    .extrude(thickness)

result = step4
