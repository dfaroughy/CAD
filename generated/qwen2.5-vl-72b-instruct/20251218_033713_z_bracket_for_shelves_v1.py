# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(7.5, 10, 50)

step2 = step1.faces(">Z").workplane().circle(5).cutThruAll()

result = step2
