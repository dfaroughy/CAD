# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base plate dimensions
length = 80.0
width = 60.0
thickness = 5.0

# Inner cutout dimensions
cutout_length = 40.0
cutout_width = 30.0

# Hole parameters
hole_diameter = 5.0
hole_offset_x = 15.0
hole_offset_y = 12.0

# Construction steps
step1 = cq.Workplane("XY").box(length, width, thickness)

step2 = (step1
         .faces(">Z")
         .workplane()
         .rect(cutout_length, cutout_width)
         .cutThruAll()
)

step3 = (step2
         .faces(">Z")
         .workplane()
         .rect(length-2*hole_offset_x, width-2*hole_offset_y)
         .vertices()
         .circle(hole_diameter/2)
         .cutThruAll()
)

result = step3
