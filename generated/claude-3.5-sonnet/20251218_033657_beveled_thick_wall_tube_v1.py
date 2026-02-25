# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
length = 50.0
height = 50.0
thickness = 5.0

# Create base plate
step1 = cq.Workplane("XY").box(length, height, thickness)

# Create circular cutout
cutout_radius = length/2 - 5
step2 = step1.faces(">Z").workplane().circle(cutout_radius).cutThruAll()

result = step2
