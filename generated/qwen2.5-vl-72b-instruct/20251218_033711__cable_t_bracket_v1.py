# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(42.5, 30, 5)

step2 = step1.faces(">Z").workplane().rect(30, 5).cutThruAll()

result = step2
