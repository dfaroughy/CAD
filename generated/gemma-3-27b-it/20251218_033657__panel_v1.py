# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(120, 60, 5)

step2 = cq.Workplane("XY").circle(5).translate((10, 30, 0))

step3 = cq.Workplane("XY").circle(3).translate((30, 30, 0))

step4 = cq.Workplane("XY").circle(3).translate((90, 30, 0))

step5 = step1.cut(step2)

step6 = step5.cut(step3)

step7 = step6.cut(step4)

result = step7
