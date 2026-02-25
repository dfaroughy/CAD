# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 40, 8)
step2 = cq.Workplane("XY").circle(4).extrude(8)
step3 = step2.translate((15, 15, 0))
step4 = step2.translate((45, 15, 0))
step5 = step2.translate((15, 25, 0))
step6 = step2.translate((45, 25, 0))
step7 = step1.union(step3, step4, step5, step6)
result = step7
