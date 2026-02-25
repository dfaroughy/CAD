# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 60, 8)

step2 = step1.faces(">Z").workplane().rect(44, 44).cutThruAll()

step3 = step2.faces(">X").workplane().center(-20, 0).rect(8, 44).cutThruAll()

step4 = step3.faces("<X").workplane().center(20, 0).rect(8, 44).cutThruAll()

result = step4
