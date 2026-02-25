# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").rect(50, 20).extrude(55)
step2 = step1.faces(">Z").workplane().rect(30, 10, forConstruction=True).vertices().circle(5).cutThruAll()
step3 = step1.faces("<Z").workplane().rect(30, 10, forConstruction=True).vertices().circle(5).cutThruAll()
result = step3
