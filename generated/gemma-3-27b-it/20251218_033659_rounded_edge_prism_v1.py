# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 40, 20)
step2 = cq.Workplane("XY").circle(10).translate((0,0,-1))
step3 = step1.cut(step2)
step4 = cq.Workplane("XY").box(60, 40, 20).translate((0,0,40))
step5 = cq.Workplane("XY").circle(10).translate((0,0,39))
step6 = step4.cut(step5)
result = step1.union(step6)
