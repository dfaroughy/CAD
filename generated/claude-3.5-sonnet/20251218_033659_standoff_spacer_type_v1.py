# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
width = 12.0
height = 10.0
thickness = 1.0

# Create base plate
step1 = (cq.Workplane("XY")
         .box(width, height, thickness)
         .faces(">Z")
         .workplane()
)

# Create outer circular pocket
step2 = (step1
         .circle(4.0)
         .cutBlind(-thickness/2)
)

# Create inner circular pocket 
step3 = (step2
         .circle(2.5)
         .cutBlind(-thickness)
)

# Create rounded corners
step4 = (step3
         .faces(">Z")
         .vertices()
         .fillet(0.5)
)

result = step4
