# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
length = 80.0
width = 40.0
height = 7.5
wall_thickness = 2.0

# Create base box with walls
step1 = (cq.Workplane("XY")
         .box(length, width, height)
         .faces(">Z")
         .shell(-wall_thickness)
)

# Create inner raised platform
platform_length = length - 2*wall_thickness - 4
platform_width = width - 2*wall_thickness - 4
platform_height = 2.0

step2 = (step1.faces("<Z")
         .workplane()
         .center(0,0)
         .rect(platform_length, platform_width)
         .extrude(platform_height)
)

# Add mounting holes
hole_diameter = 4.0
hole_spacing = 20.0

step3 = (step2.faces(">Z")
         .workplane()
         .center(0,0)
         .pushPoints([(-hole_spacing, 0), (0, 0), (hole_spacing, 0)])
         .hole(hole_diameter)
)

result = step3
