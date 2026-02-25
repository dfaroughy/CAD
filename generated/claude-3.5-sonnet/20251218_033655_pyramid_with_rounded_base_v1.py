# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main dimensions
width = 31.54
height = 31.54 
depth = 20.0

# Create base frame
step1 = (cq.Workplane("XY")
         .rect(width, height)
         .extrude(depth))

# Create inner cutout
step2 = (step1
         .faces(">Z")
         .workplane()
         .rect(width-3, height-3)
         .cutThruAll())

# Create rounded corners
radius = 1.5
step3 = (step2
         .edges("|Z")
         .fillet(radius))

# Create diagonal cross members
diagonal_width = 2.0
step4 = (cq.Workplane("XY")
         .moveTo(-width/2, -height/2)
         .lineTo(width/2, height/2)
         .moveTo(-width/2, height/2)
         .lineTo(width/2, -height/2)
         .rect(diagonal_width, diagonal_width)
         .extrude(depth))

result = step3.union(step4)
