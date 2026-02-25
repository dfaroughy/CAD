# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(12, 10, 12)
step2 = step1.faces(">Z").workplane().circle(11.999 / 2).cutThruAll()

result = step2
