# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(6.000, 20.000, 6.000)
step2 = cq.Workplane("XY").circle(3.000)
step3 = step2.extrude(6.000)
step4 = cq.Workplane("XY").box(20.000, 6.000, 6.000)
step5 = cq.Workplane("XY").box(20.000, 6.000, 6.000)

result = step1
