# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base box
step1 = cq.Workplane("XY").box(60, 40, 15)

# Step 2: Create the cutout shape
cutout_shape = (
    cq.Workplane("XY")
    .moveTo(-15, 0)
    .lineTo(-10, 0)
    .lineTo(-10, 5)
    .lineTo(10, 5)
    .lineTo(10, 0)
    .lineTo(15, 0)
    .lineTo(15, -5)
    .lineTo(-15, -5)
    .close()
    .extrude(15)
)

# Step 3: Cut the shape from the base box
step2 = step1.cut(cutout_shape)

# Step 4: Fillet the edges
result = step2.edges("|Z").fillet(5)
