# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").circle(100/2).extrude(22)
step2 = step1.faces(">Z").workplane().circle(99.999/2).cutThruAll()
step3 = step2.faces(">Z").workplane().circle(10/2).cutBlind(-5)

result = step3
