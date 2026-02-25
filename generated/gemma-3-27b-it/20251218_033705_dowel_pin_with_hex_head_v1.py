# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.rect(10.0, 10.0)
step3 = step2.extrude(10.0)
step4 = cq.Workplane("XY").transformed(offset=cq.Vector(0, 0, 10.0))
step5 = step4.polygon(points=[(2.5, 0), (5.0, 1.66), (7.5, 1.66), (10.0, 0), (7.5, -1.66), (5.0, -1.66), (2.5, 0)])
step6 = step5.extrude(2.0)
step7 = step3.union(step6)
result = step7
