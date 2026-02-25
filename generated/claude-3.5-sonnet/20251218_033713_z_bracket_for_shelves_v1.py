# model used: anthropic/claude-3.5-sonnet
# Create base rectangle
step1 = cq.Workplane("XY").box(7.5, 50.0, 10.0)

# Create circular cutout at top
step2 = step1.faces(">Z").workplane()\
    .center(0, 25.0)\
    .circle(3.75)\
    .cutThruAll()

result = step2
