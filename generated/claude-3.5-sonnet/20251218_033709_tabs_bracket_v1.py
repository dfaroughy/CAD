# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main dimensions
length = 60.0
width = 55.0
thickness = 5.0

# Base outline
step1 = (cq.Workplane("XY")
         .rect(length, width)
         .extrude(thickness))

# Cut out inner rectangle
step2 = (step1
         .faces(">Z")
         .workplane()
         .rect(length-2*thickness, width-2*thickness)
         .cutThruAll())

# Add mounting holes
hole_dia = 5.0
hole_offset = 20.0

step3 = (step2
         .faces(">Z")
         .workplane()
         .pushPoints([(hole_offset, 0), (-hole_offset, 0)])
         .hole(hole_dia))

result = step3
