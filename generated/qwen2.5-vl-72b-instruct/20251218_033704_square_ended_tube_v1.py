# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(100, 50, 50)
step2 = step1.faces(">Z").workplane().rect(40, 40).cutThruAll()
step3 = step2.faces("<Z").workplane().center(0, 25).circle(10).cutThruAll()

result = step3
