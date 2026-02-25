# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 10, 30)
step2 = cq.Workplane("XY").circle(3).extrude(30)
step3 = step2.translate((10, 0, 0))
step4 = step2.translate((70, 0, 0))
step5 = step1.cut(step3)
step6 = step5.cut(step4)
step7 = cq.Workplane("XY").box(80, 10, 30).translate((0,0,-10))
step8 = cq.Workplane("XY").circle(3).extrude(10)
step9 = step8.translate((10, 0, 0))
step10 = step8.translate((70, 0, 0))
step11 = step7.cut(step9)
step12 = step11.cut(step10)
result = step12
