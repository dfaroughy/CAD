# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").circle(12).extrude(50)
step2 = step1.faces(">Z").workplane().rect(50, 20).extrude(-20, combine=True)
step3 = step2.faces(">X").workplane().rect(4, 4).extrude(2, combine=True)
step4 = step3.faces(">Z").workplane().rect(8, 4, centered=(True, False)).extrude(-2, combine=True)
step5 = step4.faces(">Z").workplane().circle(6).extrude(-10, combine=True)

result = step5
