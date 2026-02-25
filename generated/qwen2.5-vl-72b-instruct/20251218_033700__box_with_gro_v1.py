# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(80, 60).extrude(20)

step2 = step1.faces(">Z").workplane().circle(10).cutThruAll()

step3 = step2.faces(">Z").workplane().rect(20, 5, centered=[True, False]).cutThruAll()

result = step3
