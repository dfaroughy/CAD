# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(120, 60).extrude(5)
step2 = step1.faces(">Z").workplane().circle(10).cutThruAll()
step3 = step2.faces(">Z").workplane().center(-40, 0).circle(2.5).cutThruAll()
step4 = step3.faces(">Z").workplane().center(40, 0).circle(2.5).cutThruAll()

result = step4
