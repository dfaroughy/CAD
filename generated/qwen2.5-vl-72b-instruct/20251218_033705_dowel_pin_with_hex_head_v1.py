# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").polygon(6, 10).extrude(8.66)
step2 = step1.faces(">Z").workplane().circle(8.66 / 2).extrude(26 - 8.66, combine=True)
result = step2
