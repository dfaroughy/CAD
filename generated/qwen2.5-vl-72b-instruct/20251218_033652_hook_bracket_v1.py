# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 20, 50)
step2 = step1.faces(">Z").workplane().center(-20, 0).rect(20, 20).extrude(10)
result = step2
