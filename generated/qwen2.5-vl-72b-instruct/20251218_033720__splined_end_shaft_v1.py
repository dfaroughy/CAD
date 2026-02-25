# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").polygon(6, 21.751).extrude(21.753)
step2 = step1.faces("<Z").workplane().circle(21.751 / 2).extrude(70 - 21.753, combine=True)
result = step2
