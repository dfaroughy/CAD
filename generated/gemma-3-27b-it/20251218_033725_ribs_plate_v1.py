# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(120, 97.5, 18.5)
step2 = cq.Workplane("XY").circle(5).translate((60, 48.75, 0))
step3 = cq.Workplane("XY").circle(5).translate((60, -48.75, 0))
step4 = step1.cut(step2)
step5 = step4.cut(step3)
result = step5
