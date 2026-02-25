# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 40, 20)
step2 = step1.faces(">Z").workplane().circle(5).cutThruAll()
step3 = step1.faces("<Z").workplane().rect(20, 20).cutBlind(-5)
result = step3
