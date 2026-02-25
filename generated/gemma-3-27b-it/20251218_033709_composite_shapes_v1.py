# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 40, 20)

step2 = cq.Workplane("XY").circle(5).extrude(20)
step3 = step2.translate((15, 20, 0))
step4 = cq.Workplane("XY").circle(5).extrude(20)
step5 = step4.translate((45, 20, 0))

step6 = step1.union(step3)
step7 = step6.union(step5)

step8 = cq.Workplane("XY").circle(3).extrude(5)
step9 = step8.translate((15, 20, -1))
step10 = cq.Workplane("XY").circle(3).extrude(5)
step11 = step10.translate((15, 20, 15))
step12 = cq.Workplane("XY").circle(3).extrude(5)
step13 = step12.translate((45, 20, -1))
step14 = cq.Workplane("XY").circle(3).extrude(5)
step15 = step14.translate((45, 20, 15))
step16 = step7.union(step9)
step17 = step16.union(step11)
step18 = step17.union(step13)
step19 = step18.union(step15)

result = step19
