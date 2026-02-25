# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").circle(1.0).extrude(0.2)
step2 = cq.Workplane("XY").circle(99.0).extrude(0.2)
step3 = step1.cut(step2)
step4 = cq.Workplane("XY").rect(100.0, 22.0).extrude(0.2)
step5 = step3.union(step4)

result = step5
