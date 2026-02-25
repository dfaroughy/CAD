# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 50, 5)

step2 = step1.faces("<Z").workplane().rect(40, 40).cutThruAll()

step3 = step2.faces(">X").workplane().center(-25, 0).rect(5, 50).cutThruAll()

step4 = step3.faces("<X").workplane().center(25, 0).rect(5, 50).cutThruAll()

result = step4
