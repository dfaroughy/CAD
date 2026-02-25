# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 8, 65)
step2 = step1.faces(">Z").workplane().rect(40, 4).cutThruAll()
step3 = step2.faces("<Z").workplane().rect(40, 4).cutThruAll()
step4 = step3.faces(">X").workplane().center(0, 30).circle(4).cutThruAll()
step5 = step4.faces("<X").workplane().center(0, 30).circle(4).cutThruAll()

result = step5
