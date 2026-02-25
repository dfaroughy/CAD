# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main square plate
step1 = cq.Workplane("XY").box(50, 50, 1)

# Step 2: Create the protruding trapezoidal shape
step2 = (
    cq.Workplane("XY")
    .workplane(offset=1)
    .moveTo(0, 0)
    .lineTo(27, 0)
    .lineTo(27, 50)
    .lineTo(0, 50)
    .close()
    .extrude(1)
)

# Step 3: Combine the plate and the trapezoidal shape
step3 = step1.union(step2)

# Step 4: Cut the square hole
result = step3.faces(">Z").workplane().center(10, 10).rect(10, 10).cutThruAll()
