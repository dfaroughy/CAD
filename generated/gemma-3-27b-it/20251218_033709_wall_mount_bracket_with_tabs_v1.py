# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 50, 5)
step2 = cq.Workplane("XY").circle(5).translate((0, 0, 2.5))
step3 = cq.Workplane("XY").circle(5).translate((50, 0, 2.5))
step4 = step1.cut(step2)
step5 = step4.cut(step3)
step6 = cq.Workplane("XY").box(60, 50, 5).translate((0,0,-50))
step7 = cq.Workplane("XY").circle(5).translate((0, 0, -47.5))
step8 = cq.Workplane("XY").circle(5).translate((50, 0, -47.5))
step9 = step6.cut(step7)
step10 = step9.cut(step8)
step11 = cq.Workplane("XY").box(5, 50, 5).translate((0,0,-50))
step12 = cq.Workplane("XY").box(5, 50, 5).translate((55,0,-50))
step13 = step10.cut(step11)
step14 = step13.cut(step12)
step15 = cq.Workplane("XY").box(5, 50, 5).translate((0,0,0))
step16 = cq.Workplane("XY").box(5, 50, 5).translate((55,0,0))
step17 = step14.cut(step15)
step18 = step17.cut(step16)

result = step18
