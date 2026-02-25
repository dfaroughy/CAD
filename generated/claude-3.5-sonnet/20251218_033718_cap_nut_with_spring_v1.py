# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
width = 12.0
height = 12.0
thickness = 0.999

# Create base plate
step1 = cq.Workplane("XY").box(width, height, thickness)

# Create octagonal cutout
octagon_radius = 4.0
octagon_points = []
for i in range(8):
    angle = i * 45 + 22.5  # Rotate 22.5 degrees to align flat sides
    x = octagon_radius * cos(radians(angle))
    y = octagon_radius * sin(radians(angle))
    octagon_points.append((x, y))

step2 = step1.faces(">Z").workplane()\
    .polyline(octagon_points).close()\
    .cutThruAll()

result = step2
