# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 60, 8)
step2 = (
    step1.faces(">Z")
    .workplane()
    .moveTo(-20, 30)
    .rect(40, 40)
    .cutBlind(-8)
)
step3 = (
    step2.faces(">Z")
    .workplane()
    .moveTo(-20, -30)
    .rect(10, 10)
    .cutBlind(-8)
)
step4 = (
    step3.faces(">Z")
    .workplane()
    .moveTo(20, -30)
    .rect(10, 10)
    .cutBlind(-8)
)
step5 = (
    step4.faces(">Z")
    .workplane()
    .moveTo(-20, 30)
    .rect(40, 10)
    .cutBlind(-4)
)
result = step5
