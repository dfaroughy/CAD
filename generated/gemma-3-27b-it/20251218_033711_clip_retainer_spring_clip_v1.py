# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(20, 6, 3)
step2 = cq.Workplane("XY").circle(1.5).translate((5, 0, 0))
step3 = cq.Workplane("XY").circle(1.5).translate((15, 0, 0))
step4 = step1.cutThruAll(step2)
step5 = step4.cutThruAll(step3)
result = step5
