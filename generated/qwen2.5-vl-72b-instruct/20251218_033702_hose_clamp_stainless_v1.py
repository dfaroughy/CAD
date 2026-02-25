# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(100, 8, 2)

step2 = step1.faces("<X").workplane().center(2, 0).circle(0.5).cutThruAll()

step3 = step2.faces(">X").workplane().center(-2, 0).circle(0.5).cutThruAll()

result = step3
