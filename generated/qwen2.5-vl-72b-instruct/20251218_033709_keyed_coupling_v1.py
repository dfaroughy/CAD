# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").circle(25).extrude(50)
step2 = step1.faces(">Z").workplane().rect(45, 45).extrude(-5)
step3 = step2.faces("<Z").workplane().rect(35, 35).extrude(5)
result = step3
