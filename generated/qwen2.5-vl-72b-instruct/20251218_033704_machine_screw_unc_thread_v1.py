# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").circle(4).extrude(32)
step2 = step1.faces(">Z").workplane().rect(7.999, 1.5).cutThruAll()
result = step2
