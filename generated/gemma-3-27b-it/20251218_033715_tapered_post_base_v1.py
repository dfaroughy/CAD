# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.circle(35)
step3 = step2.extrude(70)
step4 = step3.faces(">Z").workplane()
step5 = step4.circle(30)
step6 = step5.extrude(-60)
step7 = step6.faces(">Z").workplane()
step8 = step7.circle(25)
step9 = step8.extrude(-70)
step10 = step9.faces(">Z").workplane()
step11 = step10.circle(20)
step12 = step11.extrude(-90)

result = step12
