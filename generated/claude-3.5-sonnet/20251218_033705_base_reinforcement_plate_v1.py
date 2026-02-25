# model used: anthropic/claude-3.5-sonnet
# Base plate dimensions
length = 120.0
width = 80.0
thickness = 8.0

# Hole parameters
hole_diameter = 10.0
hole_offset = 10.0
center_hole_diameter = 20.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create corner holes
step2 = step1.faces(">Z").workplane()\
    .pushPoints([
        (length/2-hole_offset, width/2-hole_offset),
        (length/2-hole_offset, -width/2+hole_offset),
        (-length/2+hole_offset, width/2-hole_offset),
        (-length/2+hole_offset, -width/2+hole_offset)
    ])\
    .hole(hole_diameter, thickness)

# Create center hole
result = step2.faces(">Z").workplane()\
    .hole(center_hole_diameter, thickness)
