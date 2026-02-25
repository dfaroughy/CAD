# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(40, 20).extrude(8)
step2 = step1.faces(">Z").workplane().circle(4).cutThruAll()
step3 = step2.faces(">Z").workplane().circle(1).cutBlind(-2)

result = step3
