# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(40, 64, 15)

step2 = step1.faces("<Z").workplane().circle(5).cutThruAll()

step3 = step2.faces("<Z").workplane().center(-15, -20).circle(2.5).cutThruAll()

step4 = step3.faces("<Z").workplane().center(0, 40).circle(2.5).cutThruAll()

step5 = step4.faces("<Z").workplane().center(30, -40).circle(2.5).cutThruAll()

result = step5
