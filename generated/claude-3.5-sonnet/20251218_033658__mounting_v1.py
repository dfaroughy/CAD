# model used: anthropic/claude-3.5-sonnet
# Base dimensions
length = 60.0
width = 40.0
thickness = 8.0
corner_radius = 5.0
inner_offset = 5.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Round the corners
step2 = step1.edges("|Z").fillet(corner_radius)

# Create inner cutout with rounded corners
inner_length = length - 2*inner_offset
inner_width = width - 2*inner_offset
step3 = step2.faces(">Z").workplane()\
    .rect(inner_length, inner_width)\
    .vertices()\
    .fillet(corner_radius)\
    .cutThruAll()

# Add corner circles
circle_radius = 4.0
circle_centers = [
    (length/2-corner_radius, width/2-corner_radius),
    (length/2-corner_radius, -width/2+corner_radius),
    (-length/2+corner_radius, width/2-corner_radius),
    (-length/2+corner_radius, -width/2+corner_radius)
]

step4 = step3.faces(">Z").workplane()
for pos in circle_centers:
    step4 = step4.pushPoints([pos]).circle(circle_radius).cutThruAll()

result = step4
