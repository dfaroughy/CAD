# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(60, 50).extrude(5)

step2 = step1.faces(">Z").workplane().circle(5).cutThruAll()

step3 = step1.faces("<Z").workplane().circle(5).cutThruAll()

step4 = step1.faces(">X").workplane().center(-25, 0).circle(2.5).cutThruAll()

step5 = step1.faces("<X").workplane().center(25, 0).circle(2.5).cutThruAll()

result = step5
