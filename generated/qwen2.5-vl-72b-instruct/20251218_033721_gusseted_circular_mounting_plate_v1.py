# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").circle(100/2).extrude(10)
step2 = step1.faces(">Z").workplane().circle(10/2).cutThruAll()
step3 = step2.faces(">Z").workplane().polarArray(50, 0, 360, 3).circle(5/2).cutThruAll()

result = step3
