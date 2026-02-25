# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(125, 80).extrude(10)

step2 = step1.faces(">Z").workplane().rect(115, 70).cutThruAll()

result = step2
