# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").circle(10).extrude(95)
step2 = step1.faces(">Z").workplane().circle(8).extrude(-10, combine=True)
step3 = step2.faces("<Z").workplane().circle(8).extrude(-10, combine=True)
step4 = step3.faces(">Z").workplane().circle(6).extrude(-85, combine=True)
step5 = step4.faces("<Z").workplane().circle(6).extrude(-85, combine=True)

result = step5
