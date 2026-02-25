# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 40, 15)

step2 = step1.faces("<Z").workplane().rect(30, 20).cutThruAll()

result = step2
