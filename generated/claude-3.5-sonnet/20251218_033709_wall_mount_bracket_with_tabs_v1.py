# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main plate dimensions
length = 60.0
width = 50.0
thickness = 5.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create mounting holes
hole_dia = 5.0
hole_offset_x = length/2 - 5.0
hole_offset_y = width/2 - 5.0

step2 = step1.faces(">Z").workplane()\
    .pushPoints([
        (-hole_offset_x, hole_offset_y),
        (hole_offset_x, hole_offset_y),
        (-hole_offset_x, -hole_offset_y),
        (hole_offset_x, -hole_offset_y)
    ])\
    .hole(hole_dia)

# Create center hole
center_hole_dia = 8.0
step3 = step2.faces(">Z").workplane().hole(center_hole_dia)

# Create raised edges
edge_height = 5.0
edge_thickness = 5.0

step4 = step3.faces(">Z").workplane()\
    .rect(length, width)\
    .vertices()\
    .rect(edge_thickness, edge_thickness)\
    .extrude(edge_height)

result = step4
