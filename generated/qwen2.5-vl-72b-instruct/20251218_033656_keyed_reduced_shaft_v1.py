# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 20, 24)
step2 = step1.faces(">Z").workplane().rect(10, 4).cutThruAll()
step3 = step1.faces("<Z").workplane().rect(10, 4).cutThruAll()
result = step3
