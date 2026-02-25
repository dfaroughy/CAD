# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(60, 20).extrude(40)
step2 = step1.faces("<Z").workplane().rect(20, 20).extrude(-20)

result = step2
