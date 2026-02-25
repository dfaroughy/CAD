# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").circle(25).extrude(28)
step2 = step1.faces(">Z").workplane().circle(20).cutThruAll()
step3 = step2.faces(">Z").workplane().circle(15).cutThruAll()
step4 = step3.faces(">Z").workplane().rect(28, 28).cutThruAll()
step5 = step4.faces(">Z").workplane().rect(20, 20).cutThruAll()
step6 = step5.faces(">Z").workplane().rect(10, 10).cutThruAll()

result = step6
