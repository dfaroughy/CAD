# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(30, 20, 30)
step2 = cq.Workplane("XY").circle(10).extrude(30)
step3 = cq.Workplane("XY").circle(10).translate((10,0,0)).extrude(30)
step4 = step1.cut(step2)
step5 = step4.cut(step3)
result = step5
