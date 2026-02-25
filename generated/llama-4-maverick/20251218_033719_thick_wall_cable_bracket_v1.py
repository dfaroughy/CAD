# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 40, 15)
step2 = (
    step1.faces(">Z")
    .workplane()
    .rect(50, 30)
    .cutBlind(-10)
    .faces(">Z")
    .workplane()
    .rect(30, 20)
    .cutBlind(-5)
)
result = step2
