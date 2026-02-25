# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(120, 80, 25)
step2 = step1.faces(">Z").workplane().rect(100, 60, forConstruction=True).vertices().circle(5).cutThruAll()
result = step2
