# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 60, 8)
step2 = step1.faces(">Z").workplane().circle(20).cutThruAll()
step3 = step2.faces(">Z").workplane().pushPoints([(20, 20), (-20, 20), (-20, -20), (20, -20)]).circle(2).cutThruAll()

result = step3
