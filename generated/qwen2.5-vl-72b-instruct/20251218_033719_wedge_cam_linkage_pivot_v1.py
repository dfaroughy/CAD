# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(28.586, 8.0, 10.0)

step2 = step1.faces(">Z").workplane().circle(4.0).cutThruAll()

step3 = step1.faces("<Z").workplane().rect(12.0, 6.0, forConstruction=True).vertices().circle(0.5).cutThruAll()

result = step3
