# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main dimensions
length = 60.0
height = 50.0
thickness = 5.0
radius = 3.0

# Create base L shape
step1 = (cq.Workplane("XY")
         .hLine(length)
         .vLine(height)
         .hLine(-length)
         .vLine(-height)
         .close()
         .extrude(thickness))

# Fillet the corners
step2 = (step1
         .edges("|Z")
         .fillet(radius))

result = step2
