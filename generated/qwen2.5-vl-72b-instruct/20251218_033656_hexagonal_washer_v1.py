# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").polygon(6, 19.691).extrude(3.000)
step2 = step1.faces(">Z").workplane().circle(17.321 / 2).cutThruAll()
step3 = step2.faces("<Z").workplane().rect(3.000, 17.321).cutBlind(-3.000)

result = step3
