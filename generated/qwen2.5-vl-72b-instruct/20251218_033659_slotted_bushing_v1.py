# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").circle(15).circle(14.9995).extrude(30)
step2 = step1.faces(">Z").workplane().rect(20, 30, centered=(True, False)).extrude(-10, combine="cut")
step3 = step2.faces("<Z").workplane().rect(20, 30, centered=(True, False)).extrude(10, combine="cut")
step4 = step3.faces(">X").workplane().rect(10, 20).extrude(5, combine="cut")
step5 = step4.faces("<X").workplane().rect(10, 20).extrude(5, combine="cut")

result = step5
