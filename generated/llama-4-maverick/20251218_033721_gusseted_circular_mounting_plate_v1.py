# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Create the base cylinder
step1 = cq.Workplane("XY").circle(50).extrude(10)

# Create the central hole
step2 = step1.faces(">Z").workplane().circle(10).cutThruAll()

# Create the three peripheral holes
step3 = (
    step2.faces(">Z")
    .workplane()
    .polarArray(20, 120, 3)
    .circle(5)
    .cutThruAll()
)

result = step3
