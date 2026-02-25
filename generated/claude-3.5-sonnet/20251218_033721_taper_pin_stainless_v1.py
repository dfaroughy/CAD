# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main dimensions
length = 50.000
width = 9.979
height = 9.86
wall = 0.980

# Create base channel
step1 = (cq.Workplane("XY")
         .box(length, width, height)
         .faces(">Z")
         .shell(-wall)
)

# Create circular hole
hole_dia = 9.00
step2 = (step1.faces(">X")
         .workplane()
         .circle(hole_dia/2)
         .cutThruAll()
)

result = step2
