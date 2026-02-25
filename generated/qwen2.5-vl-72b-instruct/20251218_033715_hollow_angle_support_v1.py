# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 30, 5)

step2 = step1.faces(">Z").workplane().rect(40, 20).extrude(-5, combine='cut')

result = step2
