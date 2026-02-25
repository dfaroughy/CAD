# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 50, 5)
step2 = cq.Workplane("YZ").transformed(offset=cq.Vector(50, 0, 0)).box(5, 50, 5)
step3 = cq.Workplane("YZ").transformed(offset=cq.Vector(100, 0, 0)).box(5, 50, 5)
step4 = cq.Workplane("XY").transformed(offset=cq.Vector(0, 50, 0)).box(50, 5, 5)
step5 = step1.union(step2)
step6 = step5.union(step3)
step7 = step6.union(step4)
result = step7
