# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main dimensions
length = 50.0
width = 50.0
height = 50.0
wall_thickness = 2.0

# Create base box
step1 = cq.Workplane("XY").box(length, width, height)

# Hollow out interior
step2 = step1.faces(">Z").workplane()\
    .rect(length-2*wall_thickness, width-2*wall_thickness)\
    .cutThruAll()

# Add rounded edges on top
step3 = step2.edges("|Z and >Z").fillet(2.0)

# Add bottom reinforcement rib
step4 = step3.faces("<Z").workplane()\
    .center(0, width/4)\
    .rect(length-2*wall_thickness, wall_thickness)\
    .extrude(wall_thickness)

result = step4
