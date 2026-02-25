# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(24, 20, 50)
step2 = cq.Workplane("XY").circle(8).extrude(50)
step3 = step1.cut(step2)
step4 = cq.Workplane("XY").circle(4).extrude(20)
step5 = step4.translate((12, 0, 0))
step6 = step3.cut(step5)
result = step6
