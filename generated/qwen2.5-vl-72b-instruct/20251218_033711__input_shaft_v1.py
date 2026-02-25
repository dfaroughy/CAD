# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(95, 20, 20)
step2 = step1.faces("<X").workplane().circle(10).cutThruAll()
result = step2
