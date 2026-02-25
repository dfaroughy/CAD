# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
LENGTH = 60.0
WIDTH = 40.0
HEIGHT = 20.0
THICKNESS = 2.0

# Create base plate with rounded corners
step1 = (cq.Workplane("XY")
         .rect(LENGTH, WIDTH)
         .extrude(THICKNESS)
         .edges("|Z")
         .fillet(3.0))

# Create walls
step2 = (step1
         .faces(">Z")
         .shell(-HEIGHT)
         .edges("|Z")
         .fillet(3.0))

# Create inner lip
step3 = (cq.Workplane("XY")
         .rect(LENGTH-2*THICKNESS, WIDTH-2*THICKNESS)
         .extrude(THICKNESS)
         .translate((0,0,HEIGHT-THICKNESS))
         .edges("|Z")
         .fillet(2.0))

# Combine parts
result = step2.union(step3)
