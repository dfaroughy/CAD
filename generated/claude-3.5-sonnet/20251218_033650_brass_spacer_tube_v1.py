# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base plate dimensions
length = 12.0
width = 10.0
thickness = 1.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create rounded corners
radius = 0.5
step2 = step1.edges("|Z").fillet(radius)

# Create central circular cutout
hole_diameter = 8.0
step3 = step2.faces(">Z").workplane()\
    .circle(hole_diameter/2)\
    .cutThruAll()

# Create concentric circular grooves
groove_depths = [0.2, 0.2, 0.2]
groove_diameters = [8.4, 8.8, 9.2]

step4 = step3
for d in groove_diameters:
    step4 = step4.faces(">Z").workplane()\
        .circle(d/2)\
        .circle((d-0.4)/2)\
        .extrude(-0.2)

result = step4
