# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Dimensions
height = 30.0
diameter = 30.0
wall_thickness = 2.0
fillet_radius = 1.0

# Construction steps
step1 = (cq.Workplane("XY")
         .circle(diameter/2)
         .extrude(height))

step2 = (step1.faces(">Z")
         .shell(-wall_thickness)
         .edges("|Z")
         .fillet(fillet_radius))

result = step2
