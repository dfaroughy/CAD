# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Dimensions
width = 50.0
height = 50.0
thickness = 5.0

# Base construction
step1 = cq.Workplane("XY").box(width, height, thickness)

# Create circular cutout
cutout_diameter = 40.0
step2 = step1.faces(">Z").workplane().circle(cutout_diameter/2).cutThruAll()

result = step2
