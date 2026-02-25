# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(60, 30).extrude(15)

step2 = step1.faces("<X").workplane().rect(15, 30).extrude(-15)

result = step2
