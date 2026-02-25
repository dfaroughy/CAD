# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(120, 80).extrude(8)

step2 = step1.faces(">Z").workplane().circle(8).cutThruAll()

step3 = step2.faces(">Z").workplane().center(-56, -36).circle(4).cutThruAll()
step4 = step3.faces(">Z").workplane().center(0, 72).circle(4).cutThruAll()
step5 = step4.faces(">Z").workplane().center(112, 0).circle(4).cutThruAll()
step6 = step5.faces(">Z").workplane().center(-56, -36).circle(4).cutThruAll()

result = step6
