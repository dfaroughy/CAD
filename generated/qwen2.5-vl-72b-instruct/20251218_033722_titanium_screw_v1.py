# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(8, 8, 43)

step2 = step1.faces(">Z").workplane().circle(7.999 / 2).cutThruAll()

result = step2
