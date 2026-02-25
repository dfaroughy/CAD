# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(50, 50).extrude(50)
step2 = step1.faces("<Z").workplane().rect(40, 40).extrude(-45)

result = step2
