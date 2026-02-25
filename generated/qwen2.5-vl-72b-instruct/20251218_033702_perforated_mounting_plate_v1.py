# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 60, 5)
step2 = step1.faces("<Z").workplane().rect(40, 30).cutThruAll()
step3 = step2.faces("<Z").workplane().pushPoints([(20, 20), (-20, 20), (-20, -20), (20, -20)]).circle(2.5).cutThruAll()

result = step3
