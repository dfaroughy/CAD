# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(30, 20, 20)
step2 = cq.Workplane("XY").circle(5).translate((15, 0, 0))
step3 = step1.cut(step2)
step4 = cq.Workplane("XY").circle(2.5).translate((15, 0, 0))
step5 = step3.cut(step4)
step6 = cq.Workplane("XY").workplane(at=90).transformed(offset=cq.Vector(0, 0, 20)).circle(5).translate((15, 0, 0))
step7 = step5.cut(step6)
step8 = cq.Workplane("XY").workplane(at=90).transformed(offset=cq.Vector(0, 0, 20)).circle(2.5).translate((15, 0, 0))
step9 = step7.cut(step8)
step10 = cq.Workplane("XY").workplane(at=90).transformed(offset=cq.Vector(0, 0, -20)).circle(5).translate((15, 0, 0))
step11 = step9.cut(step10)
step12 = cq.Workplane("XY").workplane(at=90).transformed(offset=cq.Vector(0, 0, -20)).circle(2.5).translate((15, 0, 0))
step13 = step11.cut(step12)
step14 = step13.faces(">Z").workplane().chamfer(1)
step15 = step14.faces("<Z").workplane().chamfer(1)
result = step15
