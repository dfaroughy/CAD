# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 60, 40)
step2 = cq.Workplane("XY").circle(20).extrude(40)
step3 = cq.Workplane("XY").workplane(offset=10).circle(10).extrude(40)
step4 = step1.cut(step2)
step5 = step4.cut(step3)
result = step5
