# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main body dimensions
length = 60.0
width = 40.0
thickness = 20.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Add mounting holes
hole_spacing_x = 40.0
hole_spacing_y = 20.0
hole_diameter = 5.0

step2 = step1.faces(">Z").workplane()\
    .rect(hole_spacing_x, hole_spacing_y, forConstruction=True)\
    .vertices()\
    .circle(hole_diameter/2)\
    .extrude(-thickness)

# Add center slot
slot_width = 15.0
slot_length = 25.0

step3 = step2.faces(">Z").workplane()\
    .slot2D(slot_length, slot_width, 0)\
    .extrude(-thickness)

result = step3
