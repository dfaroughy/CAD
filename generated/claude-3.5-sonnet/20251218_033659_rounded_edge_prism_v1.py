# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
LENGTH = 60.0
WIDTH = 40.0
HEIGHT = 20.0
WALL = 2.0
RADIUS = 5.0

# Create base plate with rounded corners
step1 = (cq.Workplane("XY")
         .box(LENGTH, WIDTH, WALL)
         .edges("|Z")
         .fillet(RADIUS))

# Create walls
step2 = (step1.faces(">Z")
         .shell(WALL)
         .faces(">Z")
         .shell(-WALL))

# Create inner slot
step3 = (step2.faces(">Z")
         .workplane()
         .center(0, 0)
         .slot2D(20, 10, 0)
         .cutThruAll())

result = step3
