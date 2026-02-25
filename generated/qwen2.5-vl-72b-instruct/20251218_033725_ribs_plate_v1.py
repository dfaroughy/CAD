# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(120, 97.5).extrude(18.5)

step2 = step1.faces(">Z").workplane().center(-45, 0).circle(5).cutThruAll()
step3 = step2.faces(">Z").workplane().center(45, 0).circle(5).cutThruAll()

result = step3
