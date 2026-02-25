# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 60, 5)
step2 = cq.Workplane("XY").rect(70, 50)
step3 = step2.extrude(5)
step4 = step1.cut(step3)
step5 = cq.Workplane("XY").circle(3).extrude(6)
step6 = cq.Workplane("XY").transformed(offset=cq.Vector(10, 10, 0)).circle(3).extrude(6)
step7 = cq.Workplane("XY").transformed(offset=cq.Vector(70, 10, 0)).circle(3).extrude(6)
step8 = cq.Workplane("XY").transformed(offset=cq.Vector(10, 50, 0)).circle(3).extrude(6)
step9 = cq.Workplane("XY").transformed(offset=cq.Vector(70, 50, 0)).circle(3).extrude(6)
step10 = step4.union(step5)
step11 = step10.union(step6)
step12 = step11.union(step7)
step13 = step12.union(step8)
step14 = step13.union(step9)
result = step14
