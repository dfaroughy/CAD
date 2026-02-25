# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main dimensions
length = 100.0
width = 50.0
height = 100.0
wall_thickness = 5.0

# Create base box
step1 = cq.Workplane("XY").box(length, width, height)

# Create inner void
step2 = step1.faces(">Z").workplane()\
    .rect(length - 2*wall_thickness, width - 2*wall_thickness)\
    .extrude(-(height-wall_thickness))

# Create rounded cutout in bottom
step3 = step2.faces("<Z").workplane()\
    .rect(width/2, width/2)\
    .radiusArc((width/2, 0), (-width/2, 0))\
    .cutThruAll()

result = step3
