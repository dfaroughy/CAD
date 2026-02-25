# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(100, 8, 2)
step2 = cq.Workplane("XY").box(100, 8, 2).translate((0, 0, 20))
step3 = cq.Workplane("XY").box(100, 8, 2).translate((0, 0, 40))
step4 = cq.Workplane("XY").box(100, 8, 2).translate((0, 0, 60))
step5 = cq.Workplane("XY").box(100, 8, 2).translate((0, 0, 80))
result = step1.union(step2).union(step3).union(step4).union(step5)
