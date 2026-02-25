# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 15, 15)
step2 = step1.faces(">Z").workplane().center(0, -7.5).rect(15, 5).extrude(35, combine=True)
step3 = step2.faces(">Z").workplane().center(0, 7.5).rect(15, 5).extrude(35, combine=True)
step4 = step3.faces("<Z").workplane().center(0, -7.5).rect(15, 5).extrude(-35, combine=True)
step5 = step4.faces("<Z").workplane().center(0, 7.5).rect(15, 5).extrude(-35, combine=True)

result = step5
