# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(40, 64, 15)

step2 = cq.Workplane("XY").circle(5).translate((0,0,0))
step3 = step2.extrude(-15)

step4 = cq.Workplane("XY").circle(3).translate((12.5, 32, 0))
step5 = step4.extrude(-15)

step6 = cq.Workplane("XY").circle(3).translate((27.5, 32, 0))
step7 = step6.extrude(-15)

step8 = step1.cut(step3)
step9 = step8.cut(step5)
step10 = step9.cut(step7)

result = step10
