# model used: anthropic/claude-3.5-sonnet
# Base plate dimensions
length = 80.0
width = 60.0
thickness = 5.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Center the workplane on top face
step2 = step1.faces(">Z").workplane()

# Add large center hole
step3 = step2.circle(10.0).cutThrough()

# Add small hole in upper right quadrant
step4 = step3.moveTo(20, 15).circle(5.0).cutThrough()

# Add notch on right edge
step5 = step4.moveTo(length/2, 0).rect(10, 10).cutThrough()

result = step5
