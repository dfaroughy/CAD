# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
length = 60.0
width = 40.0
thickness = 15.0
corner_radius = 3.0

# Create base plate with rounded corners
step1 = (cq.Workplane("XY")
         .box(length, width, thickness)
         .edges("|Z")
         .fillet(corner_radius))

# Create inner cutout dimensions
cutout_length = 30.0
cutout_width = 20.0
cutout_radius = 2.0

# Cut out inner pocket with rounded corners
step2 = (step1
         .faces(">Z")
         .workplane()
         .rect(cutout_length, cutout_width)
         .vertices()
         .fillet(cutout_radius)
         .cutThruAll())

result = step2
