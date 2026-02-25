# model used: anthropic/claude-3.5-sonnet
# Base dimensions
width = 60.0
height = 65.0
thickness = 8.0

# Create base plate
step1 = cq.Workplane("XY").box(width, height, thickness)

# Create prongs
prong_width = 10.0
prong_height = 15.0
prong_spacing = 15.0
prong_offset = width/2 - prong_width/2 - prong_spacing/2

step2 = step1.faces(">Z").workplane().pushPoints([
    (prong_offset, height/2 - prong_height/2),
    (-prong_offset, height/2 - prong_height/2)
]).box(prong_width, prong_height, thickness)

# Create mounting holes
hole_diameter = 5.0
hole_offset = 15.0

step3 = step2.faces(">Z").workplane().pushPoints([
    (hole_offset, -height/4),
    (-hole_offset, -height/4)
]).hole(hole_diameter)

result = step3
