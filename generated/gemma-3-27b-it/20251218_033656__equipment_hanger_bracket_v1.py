# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 8, 65)
step2 = cq.Workplane("XY").transformed(offset=cq.Vector(0, 0, 57)).box(8, 8, 8)
step3 = cq.Workplane("XY").transformed(offset=cq.Vector(60-8, 0, 57)).box(8, 8, 8)
step4 = step1.cut(step2)
step5 = step4.cut(step3)
result = step5
