# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.circle(10.0).extrude(20.0)
step3 = step2.faces(">Z").workplane()
step4 = step3.circle(6.0).cutThruAll()
step5 = step2.faces(">Z").workplane(centerObject=True)
step6 = step5.rect(20.0, 40.0).extrude(20.0)
step7 = step6.faces(">Z").workplane()
step8 = step7.circle(10.0).cutThruAll()
step9 = step6.faces(">Z").workplane(centerObject=True)
step10 = step9.rect(19.99, 40.0).extrude(20.0)
step11 = step10.faces(">Z").workplane()
step12 = step11.circle(9.995).cutThruAll()
step13 = step10.faces(">Z").workplane(centerObject=True)
step14 = step13.rect(20.0, 40.0).extrude(20.0)
step15 = step14.faces(">Z").workplane()
step16 = step15.circle(10.0).cutThruAll()
step17 = step2.union(step6)
step18 = step17.union(step10)
step19 = step18.union(step14)

result = step19
