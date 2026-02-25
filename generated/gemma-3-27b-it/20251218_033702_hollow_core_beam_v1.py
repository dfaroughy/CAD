# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(200, 60, 40)
step2 = cq.Workplane("XY").transformed(offset=cq.Vector(0, 0, 40)).box(200, 60, 40)
step3 = step1.union(step2)
step4 = cq.Workplane("XY").transformed(offset=cq.Vector(20, 0, 0)).rect(160, 60)
step5 = cq.Workplane("XY").transformed(offset=cq.Vector(20, 0, 40)).rect(160, 60)
step6 = step4.extrude(40).union(step5.extrude(40))
step7 = step3.cut(step6)
result = step7
