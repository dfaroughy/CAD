# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").circle(4).extrude(8)
step2 = cq.Workplane("XY").circle(4).extrude(32)
step3 = step2.union(step1)
step4 = (
    cq.Workplane("XZ")
    .center(-16, 4)
    .rect(2, 8, centered=(True, False))
    .cutBlind(-8)
)
result = step4
