# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.box(40, 20, 60)
step3 = step2.faces(">Z").workplane()
step4 = step3.circle(5).extrude(-10)
step5 = step4.faces(">Z").workplane()
step6 = step5.circle(5).extrude(-10)
step7 = step6.faces(">Z").workplane()
step8 = step7.circle(5).extrude(-10)
step9 = step8.faces(">Z").workplane()
step10 = step9.circle(5).extrude(-10)

result = step10
