# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(40, 20, 60)
step2 = step1.faces("<X").workplane().circle(5).cutThruAll()
step3 = step2.faces("<X").workplane().center(10, 0).circle(5).cutThruAll()
step4 = step3.faces("<X").workplane().center(20, 0).circle(5).cutThruAll()

result = step4
