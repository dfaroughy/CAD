# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main pin dimensions
length = 43.0
diameter = 8.0
inner_diameter = 8.0

# Create base cylinder
step1 = cq.Workplane("XY").circle(diameter/2).extrude(length)

# Create inner hole
step2 = step1.faces(">Z").workplane().hole(inner_diameter, length)

result = step2
