# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").circle(99.999/2).extrude(10.000)
step2 = cq.Workplane("XY").circle(20.000/2).extrude(10.000)
step3 = cq.Workplane("XY").circle(40.000/2).extrude(10.000)
step4 = cq.Workplane("XY").circle(60.000/2).extrude(10.000)
step5 = step1.cut(step2)
step6 = step5.cut(step3)
step7 = step6.cut(step4)
result = step7
