# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(40, 20, 20)
step2 = step1.faces(">Z").workplane().circle(19.999 / 2).cutThruAll()
step3 = step2.faces("<Z").workplane().rect(2, 2).cutBlind(-2)
result = step3
