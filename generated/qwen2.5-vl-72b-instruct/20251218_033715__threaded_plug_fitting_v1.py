# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(30, 30, 30)
step2 = step1.faces(">Z").workplane().polygon(6, 29.999).extrude(-30, combine=False)
step3 = step1.cut(step2)

result = step3
