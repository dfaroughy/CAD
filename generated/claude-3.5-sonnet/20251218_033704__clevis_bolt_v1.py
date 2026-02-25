# model used: anthropic/claude-3.5-sonnet
# Create base block
step1 = cq.Workplane("XY").box(25, 15, 15)

# Create vertical shaft
step2 = cq.Workplane("XY").box(10, 10, 46).translate((0, 0, 15.5))

# Create hexagonal hole
step3 = step1.faces(">Z").workplane()\
    .pushPoints([(0, 0)])\
    .polygon(6, 8)\
    .cutThruAll()

# Combine parts
result = step1.union(step2).translate((0, 0, 23))
