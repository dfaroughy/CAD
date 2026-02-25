# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").circle(30).extrude(10)
step2 = step1.faces(">Z").workplane().circle(25).extrude(10)
step3 = step2.faces(">Z").workplane().circle(20).extrude(10)
step4 = step3.faces(">Z").workplane().circle(7.5).extrude(10)
step5 = step4.faces(">Z").workplane().rect(4,10).extrude(10)
step6 = step5.faces("<Z").fillet(5)
step7 = step6.edges("|Z").fillet(2)

result = step7
