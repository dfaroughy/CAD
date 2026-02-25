# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main dimensions
width = 50.0
height = 50.0
thickness = 2.0
chamfer = 5.0

# Create base rectangle
step1 = cq.Workplane("XY").box(width, height, thickness)

# Add chamfers to corners
step2 = step1.edges("|Z").chamfer(chamfer)

result = step2
