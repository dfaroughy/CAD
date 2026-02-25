# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(120, 80, 5)
step2 = step1.faces(">Z").workplane().center(-30, 0).circle(5).cutThruAll()
step3 = step2.faces(">Z").workplane().center(60, 0).circle(5).cutThruAll()
step4 = step3.faces(">Z").workplane().center(-30, 0).rect(20, 10, centered=(True, False)).cutThruAll()

result = step4
