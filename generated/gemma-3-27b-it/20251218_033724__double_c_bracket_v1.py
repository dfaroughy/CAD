# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.box(120, 40, 10)
step3 = step2.faces(">Z").workplane()
step4 = step3.rect(10, 30).center(60, 20)
step5 = step4.cutThruAll()
step6 = step2.faces(">Z").workplane()
step7 = step6.rect(10, 30).center(60, -20)
step8 = step7.cutThruAll()
result = step8
