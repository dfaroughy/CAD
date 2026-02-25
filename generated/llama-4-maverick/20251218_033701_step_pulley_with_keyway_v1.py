# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").circle(25).extrude(8)
step2 = step1.faces(">Z").workplane().circle(20).extrude(6)
step3 = step2.faces(">Z").workplane().circle(15).extrude(6)
step4 = step3.faces(">Z").workplane().circle(10).extrude(6)
step5 = step4.faces(">Z").workplane().rect(10, 4).cutBlind(-2)
step6 = step5.faces("<Z").workplane().rect(10, 4).cutBlind(2)

result = step6
