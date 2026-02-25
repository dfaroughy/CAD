# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
width = 50.0
height = 28.0
depth = 50.0

# Create base plate
step1 = cq.Workplane("XY").box(width, depth, height)

# Create first level cutout
step2 = step1.faces(">Z").workplane()\
    .rect(width-10, depth-10)\
    .cutBlind(-height/3)

# Create second level cutout  
step3 = step2.faces(">Z").workplane()\
    .rect(width-20, depth-20)\
    .cutBlind(-height/3)

# Create center hole
step4 = step3.faces(">Z").workplane()\
    .circle(5)\
    .cutThruAll()

result = step4
