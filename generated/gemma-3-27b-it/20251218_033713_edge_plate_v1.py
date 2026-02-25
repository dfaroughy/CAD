# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.box(80, 5, 60)
step3 = step2.faces(">Z").workplane()
step4 = step3.hole(5)
step5 = step4.translate((60, 0, 0))
step6 = step5.hole(5)
step7 = step2.faces(">Z").workplane()
step8 = step7.translate((0, 0, 55))
step9 = step8.hole(5)
step10 = step9.translate((60, 0, 0))
step11 = step10.hole(5)

result = step11
