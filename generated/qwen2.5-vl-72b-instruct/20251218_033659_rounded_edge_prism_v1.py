# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 40, 20)
step2 = step1.faces(">Z").workplane().rect(20, 10).cutThruAll()
step3 = step2.faces("<Z").workplane().rect(20, 10).cutThruAll()
step4 = step3.faces(">X").workplane().rect(10, 20).cutThruAll()
step5 = step4.faces("<X").workplane().rect(10, 20).cutThruAll()

result = step5
