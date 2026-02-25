# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(31.540, 31.540).extrude(20.000)
step2 = step1.faces(">Z").workplane().rect(20.000, 20.000).extrude(-20.000, True)
step3 = step2.faces("<Z").workplane().circle(10.000).extrude(20.000, True)
result = step3
