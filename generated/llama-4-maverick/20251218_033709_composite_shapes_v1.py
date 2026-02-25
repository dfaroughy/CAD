# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 40, 20)
step2 = (
    step1.faces(">Z")
    .workplane()
    .pushPoints([(15, 10), (15, -10), (-15, 10), (-15, -10)])
    .cboreHole(6, 10, 10)
)
step3 = step2.faces(">Z").workplane().center(0, 0).hole(16)
result = step3
