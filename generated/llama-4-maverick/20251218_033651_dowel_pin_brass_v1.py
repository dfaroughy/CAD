# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").circle(3).extrude(20)
step2 = step1.faces(">Z").workplane().rect(6, 20, centered=False).extrude(6)
step3 = step2.faces(">X").workplane().rect(20, 6, centered=False).extrude(6)
step4 = step3.faces(">Y").workplane().rect(20, 6, centered=False).extrude(6)

result = step4
