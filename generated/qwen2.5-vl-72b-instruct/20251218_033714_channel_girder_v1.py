# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 50, 5)

step2 = step1.faces("<X").workplane().rect(5, 50).cutThruAll()

result = step2
