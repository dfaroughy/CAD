# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(40, 20, 51.252)
step2 = step1.faces(">Z").workplane().circle(10).cutThruAll()
step3 = step1.faces("<Z").workplane().rect(20, 20, forConstruction=True).vertices().circle(1).extrude(51.252)

result = step3
