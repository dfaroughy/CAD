# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.box(100, 50, 50)
step3 = step2.faces(">Z").workplane()
step4 = step3.center(25, 25)
step5 = step4.circle(25)
step6 = step5.extrude(-50)
step7 = step2.cut(step6)
result = step7
