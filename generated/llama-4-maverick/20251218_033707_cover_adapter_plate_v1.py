# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 60, 8, centered=(True, True, False))
step2 = step1.faces(">Z").workplane().circle(20).cutThruAll()
step3 = (
    step2.faces(">Z")
    .workplane()
    .pushPoints([(20, 20), (-20, 20), (-20, -20), (20, -20)])
    .circle(5)
    .cutThruAll()
)
result = step3
