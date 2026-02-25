# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(30, 30, 90)
step2 = step1.faces(">Z").workplane().circle(20).cutThruAll()
step3 = step2.faces("<Z").workplane().rect(29.999, 40).cutThruAll()

result = step3
