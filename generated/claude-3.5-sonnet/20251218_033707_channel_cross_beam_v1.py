# model used: anthropic/claude-3.5-sonnet
# Create rectangular frame
step1 = cq.Workplane("XY").box(200, 60, 10)

# Create inner cutout
step2 = step1.faces(">Z").workplane().box(180, 40, 10).cut()

result = step2
