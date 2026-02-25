# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(80, 60, centered=False).vertices().fillet(5)
step2 = step1.extrude(5)
step3 = (
    step2.faces(">Z")
    .workplane()
    .pushPoints([(10, 10), (70, 10), (10, 50), (70, 50)])
    .circle(3)
    .cutThruAll()
)
result = step3
