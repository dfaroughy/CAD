# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(120, 80, 5)
step2 = cq.Workplane("XY").circle(5).translate((30, 40, 0))
step3 = cq.Workplane("XY").circle(5).translate((90, 40, 0))
step4 = step1.cut(step2)
step5 = step4.cut(step3)
result = step5
