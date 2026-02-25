# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").polygon(8, 12).extrude(12)
step2 = step1.faces(">Z").workplane().circle(11.999 / 2).cutThruAll()
step3 = step2.faces("<Z").workplane().rect(12, 12, forConstruction=True).vertices().circle(1.5).cutThruAll()

result = step3
