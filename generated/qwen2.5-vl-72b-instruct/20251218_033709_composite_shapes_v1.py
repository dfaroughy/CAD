# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 40, 20)

step2 = step1.faces(">Z").workplane().circle(10).cutThruAll()

step3 = step2.faces(">Z").workplane().rect(20, 40, forConstruction=True).vertices().circle(5).cutThruAll()

step4 = step3.faces("<Z").workplane().rect(20, 40, forConstruction=True).vertices().circle(5).cutThruAll()

result = step4
