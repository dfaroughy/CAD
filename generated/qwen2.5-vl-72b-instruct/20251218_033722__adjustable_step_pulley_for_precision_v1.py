# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").circle(60/2).extrude(10)
step2 = step1.faces(">Z").workplane().circle(50/2).extrude(10)
step3 = step2.faces(">Z").workplane().circle(40/2).extrude(10)
step4 = step3.faces(">Z").workplane().circle(30/2).extrude(10)
step5 = step4.faces(">Z").workplane().circle(20/2).extrude(10)
step6 = step5.faces(">Z").workplane().circle(10/2).extrude(10)

result = step6
