# model used: anthropic/claude-3.5-sonnet
# Create rectangular tube profile
step1 = cq.Workplane("XY").box(60.0, 9.0, 5.0)
step2 = step1.faces(">Z").shell(-1.0)  # Shell with 1mm wall thickness

result = step2
