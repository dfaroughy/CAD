# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").polygon(4, 50).extrude(25)
step2 = step1.faces(">Z").workplane().center(-25, 0).polygon(3, 50).extrude(25, combine=True)
step3 = step2.faces(">Z").workplane().center(25, 0).polygon(3, 50).extrude(25, combine=True)
result = step3
