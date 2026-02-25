# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(25, 25, 15)
step2 = step1.faces(">Z").workplane().polygon(6, 10).extrude(-5, both=True)
step3 = step2.faces("<Z").workplane().center(0, 12.5).rect(5, 5).extrude(46)
result = step3
