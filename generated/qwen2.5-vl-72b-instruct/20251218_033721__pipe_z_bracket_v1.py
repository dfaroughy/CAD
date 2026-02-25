# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(10, 7.5).extrude(50)

step2 = step1.faces(">Z").workplane().rect(8, 5.5).cutThruAll()

result = step2
