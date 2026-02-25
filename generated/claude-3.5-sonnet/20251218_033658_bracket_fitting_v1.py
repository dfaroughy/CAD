# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main dimensions
length = 60.0
width = 40.0
thickness = 15.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create rounded corner
radius = 5.0
step2 = step1.edges("|Z and >Y").fillet(radius)

result = step2
