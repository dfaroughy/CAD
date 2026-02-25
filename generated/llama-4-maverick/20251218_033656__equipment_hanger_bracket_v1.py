# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 59, 8)
step2 = (
    step1.faces(">Z")
    .workplane()
    .moveTo(0, 14)
    .rect(20, 20)
    .cutBlind(-8)
)
step3 = (
    step2.faces(">Z")
    .workplane()
    .moveTo(-20, -14)
    .circle(5)
    .cutBlind(-8)
)
step4 = (
    step3.faces(">Z")
    .workplane()
    .moveTo(20, -14)
    .circle(5)
    .cutBlind(-8)
)
step5 = (
    step4.faces(">Z")
    .workplane()
    .moveTo(0, 0)
    .rect(8, 35)
    .extrude(8)
)
result = step5
