# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(70, 70).extrude(90)
step2 = step1.faces(">Z").workplane().rect(90, 90).extrude(-90, combine=False)
step3 = step1.cut(step2)
step4 = step3.faces(">Z").workplane().circle(30).extrude(-90, combine=False)
result = step3.cut(step4)
