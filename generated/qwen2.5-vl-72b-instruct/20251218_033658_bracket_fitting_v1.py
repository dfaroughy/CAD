# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(60, 40).extrude(15)

step2 = step1.faces("<Z").workplane().rect(15, 40).cutThruAll()

result = step2
