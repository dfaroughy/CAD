# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 50, 15)
step2 = step1.faces(">Z").workplane().rect(40, 40).cutBlind(-5)
step3 = step2.faces("<Z").workplane().rect(40, 40).cutBlind(5)
result = step3
