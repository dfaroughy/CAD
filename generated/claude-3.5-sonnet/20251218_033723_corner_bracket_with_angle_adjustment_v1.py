# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
LENGTH = 60.0
WIDTH = 8.0
HEIGHT = 60.0

# Create base plate
step1 = cq.Workplane("XY").box(LENGTH, WIDTH, HEIGHT)

# Create cutout profile
step2 = (cq.Workplane("XY")
         .moveTo(-LENGTH/4, 0)
         .vLine(HEIGHT/2)
         .hLine(LENGTH/2)
         .vLine(-HEIGHT/4)
         .hLine(LENGTH/4)
         .vLine(-HEIGHT/4)
         .hLine(-LENGTH/2)
         .close()
         .extrude(WIDTH)
)

# Subtract cutout from base
result = step1.cut(step2)
