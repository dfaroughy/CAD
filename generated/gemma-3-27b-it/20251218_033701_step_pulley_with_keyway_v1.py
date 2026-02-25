# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 50, 28)
step2 = cq.Workplane("XY").transformed(offset=cq.Vector(0, 0, 28)).box(50, 50, 28)
step3 = cq.Workplane("XY").transformed(offset=cq.Vector(0, 0, 56)).box(50, 50, 28)
step4 = cq.Workplane("XY").transformed(offset=cq.Vector(0, 0, 84)).box(50, 50, 28)

step5 = cq.Workplane("XY").circle(25).extrude(28)
step6 = cq.Workplane("XY").transformed(offset=cq.Vector(0, 0, 28)).circle(25).extrude(28)
step7 = cq.Workplane("XY").transformed(offset=cq.Vector(0, 0, 56)).circle(25).extrude(28)
step8 = cq.Workplane("XY").transformed(offset=cq.Vector(0, 0, 84)).circle(25).extrude(28)

step9 = step1.union(step2)
step10 = step9.union(step3)
step11 = step10.union(step4)
step12 = step5.union(step6)
step13 = step12.union(step7)
step14 = step13.union(step8)
step15 = step11.union(step14)

result = step15
