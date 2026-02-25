# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
length = 64.0
width = 40.0
thickness = 15.0
hole_dia = 5.0
center_hole_dia = 15.0

# Create base plate
step1 = cq.Workplane("XY").box(width, length, thickness)

# Add mounting holes in corners
hole_spacing_x = 30.0
hole_spacing_y = 54.0
step2 = step1.faces(">Z").workplane()\
    .rect(hole_spacing_x, hole_spacing_y, forConstruction=True)\
    .vertices()\
    .hole(hole_dia)

# Add center hole
step3 = step2.faces(">Z").workplane()\
    .hole(center_hole_dia)

# Add raised section on top
boss_width = 10.0
boss_length = 10.0 
boss_height = 5.0
step4 = step3.faces(">Z").workplane()\
    .center(0, length/4)\
    .box(boss_width, boss_length, boss_height)

result = step4
