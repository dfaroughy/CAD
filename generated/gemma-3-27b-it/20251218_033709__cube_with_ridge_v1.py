# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 15, 50)
step2 = cq.Workplane("XY").box(50, 15, 50).translate((0, 0, 50))
step3 = cq.Workplane("XY").box(15, 50, 50)
step4 = cq.Workplane("XY").box(15, 50, 50).translate((50, 0, 0))
step5 = cq.Workplane("XY").box(15, 50, 50).translate((50, 0, 50))
step6 = cq.Workplane("XY").box(15, 50, 50).translate((0, 0, 50))
step7 = step1.union(step2)
step8 = step3.union(step4)
step9 = step5.union(step6)
result = step7.union(step8).union(step9)
