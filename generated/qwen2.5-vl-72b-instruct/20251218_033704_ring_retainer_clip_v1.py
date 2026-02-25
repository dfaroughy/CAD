# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(30, 3, 30)
step2 = step1.faces("<X").workplane().circle(29.999/2).cutThruAll()
step3 = step2.faces(">X").workplane().rect(3, 3).cutThruAll()

result = step3
