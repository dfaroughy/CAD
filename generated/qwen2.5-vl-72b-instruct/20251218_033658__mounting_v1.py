# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(60, 40).extrude(8)
step2 = step1.faces(">Z").workplane().circle(4).cutThruAll()
step3 = step2.faces(">Z").workplane().center(-20, 0).circle(4).cutThruAll()
step4 = step3.faces(">Z").workplane().center(40, 0).circle(4).cutThruAll()
step5 = step4.faces(">Z").workplane().center(-40, 0).circle(4).cutThruAll()

result = step5
