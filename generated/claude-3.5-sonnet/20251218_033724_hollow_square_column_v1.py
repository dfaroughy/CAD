# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main dimensions
length = 100.0
width = 50.0
height = 50.0
thickness = 5.0

# Create base profile
step1 = (cq.Workplane("XY")
         .rect(length, width)
         .extrude(thickness))

# Create outer walls
step2 = (step1
         .faces(">Z")
         .rect(length-thickness, width-thickness)
         .extrude(height-thickness))

# Create inner cutout
step3 = (step2
         .faces(">Z")
         .rect(length-3*thickness, width-3*thickness)
         .cutThruAll())

# Add mounting holes
step4 = (step3
         .faces(">Z")
         .workplane()
         .pushPoints([(-length/4, 0), (length/4, 0)])
         .hole(thickness))

result = step4
