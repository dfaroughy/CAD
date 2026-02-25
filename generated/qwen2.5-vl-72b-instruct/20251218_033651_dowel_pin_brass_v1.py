# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(20, 6).extrude(6)
step2 = step1.faces(">Z").workplane().circle(3).cutThruAll()

result = step2
