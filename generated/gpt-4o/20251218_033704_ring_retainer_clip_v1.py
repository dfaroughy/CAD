# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base cylinder
step1 = cq.Workplane("XY").circle(15).extrude(3)

# Step 2: Create the keyhole shape
step2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .circle(3)
    .extrude(3)
    .faces(">Z")
    .workplane()
    .moveTo(0, 0)
    .rect(6, 3)
    .cutBlind(-3)
)

# Step 3: Combine the keyhole with the base cylinder
result = step1.cut(step2)
