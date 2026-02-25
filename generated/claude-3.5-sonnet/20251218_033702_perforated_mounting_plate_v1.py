# model used: anthropic/claude-3.5-sonnet
# Base plate dimensions
length = 80.0
width = 60.0
thickness = 5.0

# Hole and cutout parameters
hole_diameter = 5.0
hole_offset = 7.0
cutout_width = 30.0
cutout_height = 20.0
cutout_offset = 5.0

# Construction steps
step1 = cq.Workplane("XY").box(length, width, thickness)

step2 = step1.faces(">Z").workplane()\
    .rect(length-2*hole_offset, width-2*hole_offset, forConstruction=True)\
    .vertices()\
    .circle(hole_diameter/2)\
    .cutThruAll()

step3 = step2.faces(">Z").workplane()\
    .rect(cutout_width, cutout_height)\
    .cutThruAll()

result = step3.translate((0,0,-thickness/2))
