# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main block
step1 = cq.Workplane("XY").box(60, 15, 30)

# Step 2: Create the cutout shape
cutout = (
    cq.Workplane("XY")
    .moveTo(30, 0)
    .lineTo(45, 0)
    .lineTo(45, 7.5)
    .lineTo(60, 7.5)
    .lineTo(60, 15)
    .lineTo(30, 15)
    .close()
    .extrude(30)
)

# Step 3: Cut the shape from the main block
step2 = step1.cut(cutout)

# Assign final result
result = step2
