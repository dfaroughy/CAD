# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 70, 25)
step2 = cq.Workplane("XY").circle(5).translate((40, 35, 0))
step3 = cq.Workplane("XY").circle(5).translate((40, 35, 25))
step4 = step1.cut(cq.Workplane("XY").workplane(offset=1).hole(5))
step5 = step1.cut(cq.Workplane("XY").workplane(offset=25).hole(5))
step6 = cq.Workplane("XY").transformed(offset=cq.Vector(0,0,70)).box(80, 25, 25)
step7 = step6.cut(cq.Workplane("XY").workplane(offset=1).hole(5))
step8 = step6.cut(cq.Workplane("XY").workplane(offset=25).hole(5))
step9 = step1.union(step8)

result = step9
