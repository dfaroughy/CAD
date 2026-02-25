# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(80, 60).extrude(5)

step2 = step1.faces("<Z").workplane().split(keepBottom=True).rect(70, 50).cutThruAll()

step3 = step2.faces("<Z").workplane().split(keepBottom=True).rect(60, 40).cutThruAll()

step4 = step3.faces("<Z").workplane().center(-20, 0).circle(2.5).cutThruAll()

step5 = step4.faces("<Z").workplane().center(40, 0).slot2Point((-10, 0), (10, 0), 15).cutThruAll()

step6 = step5.faces("<Z").workplane().center(20, 0).slot2Point((-10, 0), (10, 0), 15).cutThruAll()

result = step6
