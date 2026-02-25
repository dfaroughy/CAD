# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main dimensions
diameter = 100.0
height = 86.603
base_width = 30.0
base_height = 10.0

# Create the main spherical body with flat top and bottom
step1 = (cq.Workplane("XY")
         .circle(diameter/2)
         .extrude(height)
         .faces(">Z")
         .chamfer(10)
         .faces("<Z")
         .chamfer(10))

# Create the base
step2 = (cq.Workplane("XY")
         .rect(base_width, base_height)
         .extrude(base_height)
         .edges("|Z")
         .fillet(2))

# Position and combine
result = (step1
          .union(step2.translate((0, 0, -base_height/2))))
