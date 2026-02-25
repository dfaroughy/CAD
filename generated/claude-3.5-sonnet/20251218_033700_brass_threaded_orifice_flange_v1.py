# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
diameter = 100
height = 22
center_hole_dia = 10

# Create base cylinder
step1 = cq.Workplane("XY").circle(diameter/2).extrude(height)

# Add center hole
step2 = step1.faces(">Z").workplane().hole(center_hole_dia)

# Add decorative circular grooves
groove_depth = 1
groove_width = 2
groove_radii = [30, 40, 45]

step3 = step2
for radius in groove_radii:
    step3 = step3.faces(">Z").workplane() \
        .circle(radius).circle(radius-groove_width) \
        .cutBlind(-groove_depth)

result = step3
