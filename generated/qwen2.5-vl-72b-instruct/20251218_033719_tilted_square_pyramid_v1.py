# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 50, 27)
step2 = step1.faces(">Z").workplane().rect(10, 10).cutThruAll()
result = step2
