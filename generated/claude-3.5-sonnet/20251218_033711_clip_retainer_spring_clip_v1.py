# model used: anthropic/claude-3.5-sonnet
# Base dimensions
length = 20.0
width = 6.0
thickness = 3.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create circular holes
hole_diameter = 2.0
hole_centers_x = 15.0  # Distance between hole centers
step2 = step1.faces(">Z").workplane()\
    .pushPoints([(-hole_centers_x/2, 0), (hole_centers_x/2, 0)])\
    .hole(hole_diameter)

# Create center cutout
cutout_length = 8.0
cutout_width = 2.0
step3 = step2.faces(">Z").workplane()\
    .rect(cutout_length, cutout_width)\
    .cutThruAll()

result = step3
