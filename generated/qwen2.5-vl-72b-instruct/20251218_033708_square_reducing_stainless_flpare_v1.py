# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(100, 100, 20)
step2 = step1.faces("<Z").workplane().circle(30).cutThruAll()
step3 = step2.faces("<Z").workplane().rect(60, 60, forConstruction=True).vertices().circle(5).cutThruAll()

result = step3
