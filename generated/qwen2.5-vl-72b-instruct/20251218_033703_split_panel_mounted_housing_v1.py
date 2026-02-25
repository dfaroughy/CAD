# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(80, 25).extrude(60)
step2 = step1.faces("<Z").workplane().rect(50, 20).extrude(-40)
result = step2
