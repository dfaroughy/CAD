# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(120, 80, 25)
step2 = cq.Workplane("XY").circle(5).translate((15, 15, 0))
step3 = cq.Workplane("XY").circle(5).translate((15, 65, 0))
step4 = cq.Workplane("XY").circle(5).translate((105, 15, 0))
step5 = cq.Workplane("XY").circle(5).translate((105, 65, 0))
step6 = step1.cut(cq.Workplane("XY").transformed(offset=cq.Vector(0,0,1)).hole(step2))
step7 = step6.cut(cq.Workplane("XY").transformed(offset=cq.Vector(0,0,1)).hole(step3))
step8 = step7.cut(cq.Workplane("XY").transformed(offset=cq.Vector(0,0,1)).hole(step4))
step9 = step8.cut(cq.Workplane("XY").transformed(offset=cq.Vector(0,0,1)).hole(step5))
result = step9
