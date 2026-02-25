# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(200, 60, 40, centered=(True, True, False))
step2 = (
    step1.faces(">Z")
    .workplane(centerOption="CenterOfMass")
    .pushPoints([(50, 0), (-50, 0)])
    .circle(10)
    .cutThruAll()
)
step3 = (
    step2.faces(">Y")
    .workplane(centerOption="CenterOfMass")
    .rect(180, 20)
    .cutThruAll()
)
result = step3
