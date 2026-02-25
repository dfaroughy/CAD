# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main body dimensions
width = 40.0
height = 75.0
thickness = 5.0

# Create base plate
step1 = cq.Workplane("XY").box(width, height, thickness)

# Add rounded corners on bottom
step2 = step1.edges("|Z").filter(lambda e: e.Center().y < 0).fillet(2.5)

# Create top rounded section
step3 = step2.faces(">Z").workplane()\
    .center(0, height/2 - thickness)\
    .circle(thickness/2)\
    .extrude(thickness)

# Add cutout in middle
cutout_width = 10
cutout_height = 15
step4 = step3.faces(">Z").workplane()\
    .center(0, -height/4)\
    .rect(cutout_width, cutout_height)\
    .cutThruAll()

result = step4
