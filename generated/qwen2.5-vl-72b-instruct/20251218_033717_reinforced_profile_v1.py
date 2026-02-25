# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(100, 60, 40)

step2 = step1.faces(">Z").workplane().circle(10).cutThruAll()

step3 = step2.faces("<Z").workplane().rect(20, 60, centered=(False, True)).extrude(10, combine='cut')

result = step3
