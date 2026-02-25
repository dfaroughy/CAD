# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(40, 75, 5)

step2 = step1.faces(">Z").workplane().rect(20, 5).cutThruAll()

step3 = step2.faces(">X").workplane().center(0, -35).circle(2.5).cutThruAll()

result = step3
