# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
width = 60.0
height = 50.0
thickness = 20.0

# Create base rectangular prism with rounded corners
step1 = (cq.Workplane("XY")
         .box(width, height, thickness)
         .edges("|Z")
         .fillet(2.0))

# Create top mounting block
block_width = 15.0
block_height = 10.0
block_thickness = thickness

step2 = (cq.Workplane("XY")
         .box(block_width, block_height, block_thickness)
         .translate((0, height/2 + block_height/2, 0)))

# Combine base and mounting block
result = step1.union(step2)
