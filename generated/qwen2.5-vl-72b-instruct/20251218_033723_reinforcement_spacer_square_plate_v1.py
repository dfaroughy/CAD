# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 80, 10)

step2 = step1.faces("<Z").workplane().rect(40, 40, forConstruction=True).vertices().circle(5).cutThruAll()

result = step2
