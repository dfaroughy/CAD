# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(120, 80).extrude(5)
step2 = step1.faces("<Z").workplane().pushPoints([(30, 20), (-30, 20), (30, -20), (-30, -20)]).circle(5).cutThruAll()
result = step2
