# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(200, 60, 40)
step2 = step1.faces(">Z").workplane().circle(20).cutThruAll()
result = step2
