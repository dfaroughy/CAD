# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(30, 20).extrude(39.124)
step2 = step1.faces(">Z").workplane().circle(29.999 / 2).cutThruAll()
step3 = step2.faces("<Z").workplane().polygon(6, 29.999).extrude(39.124)

result = step3
