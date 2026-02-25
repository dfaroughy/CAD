# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").circle(10).extrude(40)
step2 = step1.faces(">Z").workplane().circle(8).extrude(-20)
step3 = step2.faces("<Z").workplane().circle(6).extrude(-10)
step4 = step3.faces(">Z").workplane().rect(20,20).extrude(10)
step5 = step4.faces(">Z").workplane().rect(6,6).extrude(10)
step6 = step5.faces("<Z").workplane().rect(6,6).extrude(-10)
step7 = step6.faces("<Z").workplane().rect(20,20).extrude(-10)
step8 = step7.faces(">Y").workplane().rect(2,40).extrude(2)
step9 = step8.faces("<Y").workplane().rect(2,40).extrude(-2)
step10 = step9.faces(">X").workplane().rect(20,2).extrude(2)
step11 = step10.faces("<X").workplane().rect(20,2).extrude(-2)

result = step11
