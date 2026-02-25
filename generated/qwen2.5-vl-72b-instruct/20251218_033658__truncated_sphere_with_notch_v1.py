# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").circle(100/2).extrude(86.603)
step2 = step1.faces(">Z").workplane().circle(99.999/2).cutThruAll()
result = step2
