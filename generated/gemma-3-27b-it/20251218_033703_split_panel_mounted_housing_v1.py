# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.box(80.00, 60.00, 25.00)
step3 = step2.faces(">Z").workplane()
step4 = step3.center(40.00, 30.00).rect(70.00, 50.00)
step5 = step4.cutThruAll()
step6 = step2.faces(">Z").workplane(0.00)
step7 = step6.center(40.00, 30.00).rect(70.00, 50.00)
step8 = step7.cutThruAll()
result = step8
