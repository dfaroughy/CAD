# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 80, 10)
step2 = cq.Workplane("XY").circle(5).translate((20, 20, 0))
step3 = cq.Workplane("XY").circle(5).translate((60, 20, 0))
step4 = cq.Workplane("XY").circle(5).translate((20, 60, 0))
step5 = cq.Workplane("XY").circle(5).translate((60, 60, 0))
step6 = step1.cut(cq.Workplane("XY").transformed(offset=cq.Vector(0,0,1)).hole(5, h=11, center=(20,20)))
step7 = step6.cut(cq.Workplane("XY").transformed(offset=cq.Vector(0,0,1)).hole(5, h=11, center=(60,20)))
step8 = step7.cut(cq.Workplane("XY").transformed(offset=cq.Vector(0,0,1)).hole(5, h=11, center=(20,60)))
step9 = step8.cut(cq.Workplane("XY").transformed(offset=cq.Vector(0,0,1)).hole(5, h=11, center=(60,60)))
step10 = cq.Workplane("XY").box(80, 80, 10).translate((0,0,86))
step11 = cq.Workplane("XY").box(80, 10, 80).translate((0,0,10))
step12 = step9.union(step10)
step13 = step12.union(step11)

result = step13
