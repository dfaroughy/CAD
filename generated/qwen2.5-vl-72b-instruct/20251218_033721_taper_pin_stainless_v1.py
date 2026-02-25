# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(50.000, 9.980).extrude(9.979)

step2 = step1.faces("<Z").workplane().circle(9.980 / 2).cutThruAll()

result = step2
