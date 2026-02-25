# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 25, 25)
step2 = step1.faces(">Z").workplane().center(-25, 0).rect(10, 25).cutThruAll()
step3 = step2.faces(">Z").workplane().center(25, 0).rect(10, 25).cutThruAll()
step4 = step3.faces("<Z").workplane().center(-25, 0).rect(10, 25).cutThruAll()
step5 = step4.faces("<Z").workplane().center(25, 0).rect(10, 25).cutThruAll()
step6 = step5.faces("<X").workplane().center(0, 12.5).circle(5).cutThruAll()
step7 = step6.faces("<X").workplane().center(0, -12.5).circle(5).cutThruAll()
step8 = step7.faces(">X").workplane().center(0, 0).rect(25, 70).extrude(25)

result = step8
