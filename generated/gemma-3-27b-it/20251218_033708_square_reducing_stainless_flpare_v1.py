# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.box(100, 100, 20)
step3 = step2.faces(">Z").workplane()
step4 = step3.circle(20)
step5 = step4.cutThruAll()
step6 = step2.faces(">Z").workplane()
step7 = step6.center(25, 25).circle(5)
step8 = step7.cutThruAll()
step9 = step2.faces(">Z").workplane()
step10 = step9.center(-25, 25).circle(5)
step11 = step10.cutThruAll()
step12 = step2.faces(">Z").workplane()
step13 = step12.center(25, -25).circle(5)
step14 = step13.cutThruAll()
step15 = step2.faces(">Z").workplane()
step16 = step15.center(-25, -25).circle(5)
step17 = step16.cutThruAll()
result = step17
