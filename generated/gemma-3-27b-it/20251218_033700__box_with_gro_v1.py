# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 60, 20)
step2 = cq.Workplane("XY").circle(10).extrude(20)
step3 = cq.Workplane("XY").transformed(offset=cq.Vector(40, 30, 0)).circle(10).extrude(20)
step4 = step1.union(step2)
step5 = step4.union(step3)
result = step5
