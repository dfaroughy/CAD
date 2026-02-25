# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(20, 6, 3)

step2 = step1.faces("<X").workplane().circle(1.5).cutThruAll()

step3 = step2.faces(">X").workplane().circle(1.5).cutThruAll()

result = step3
