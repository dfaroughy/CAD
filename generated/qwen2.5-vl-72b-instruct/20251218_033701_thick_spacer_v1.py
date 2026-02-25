# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").circle(20).circle(15).extrude(15)
step2 = step1.faces("<Z").workplane().circle(10).cutThruAll()

result = step2
