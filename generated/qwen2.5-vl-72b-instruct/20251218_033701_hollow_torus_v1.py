# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").circle(20).circle(15).extrude(50)
step2 = step1.faces("<Z").workplane().circle(5).extrude(50, combine=False)
step3 = step1.cut(step2)

result = step3
