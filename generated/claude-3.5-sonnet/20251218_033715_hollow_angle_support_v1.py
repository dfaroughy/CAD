# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
width = 50.0
depth = 30.0
height = 50.0
thickness = 2.0

# Create base plate
step1 = cq.Workplane("XY").box(width, depth, thickness)

# Create back plate
step2 = cq.Workplane("XY").box(width, thickness, height).translate((0, depth/2-thickness/2, height/2))

# Create side walls
step3 = cq.Workplane("XY").box(thickness, depth, height).translate((width/2-thickness/2, 0, height/2))
step4 = cq.Workplane("XY").box(thickness, depth, height).translate((-width/2+thickness/2, 0, height/2))

# Combine all parts
result = step1.union(step2).union(step3).union(step4)
