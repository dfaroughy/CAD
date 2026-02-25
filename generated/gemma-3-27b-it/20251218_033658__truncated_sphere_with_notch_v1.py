# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").circle(49.9995).extrude(86.003)
step2 = cq.Workplane("XY").circle(4.9995).extrude(1.0)
step3 = cq.Workplane("XY").transformed(offset=cq.Vector(0, 0, 85.003)).circle(49.9995).extrude(-1.0)
step4 = step1.union(step2)
result = step4.cut(step3)
