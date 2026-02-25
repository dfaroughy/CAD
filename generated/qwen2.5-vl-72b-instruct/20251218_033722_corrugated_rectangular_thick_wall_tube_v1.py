# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(100, 60).extrude(50)

step2 = step1.faces("<Z").workplane().rect(80, 40).cutThruAll()

step3 = step2.faces(">Z").workplane().center(-20, 0).circle(10).cutThruAll()

result = step3
