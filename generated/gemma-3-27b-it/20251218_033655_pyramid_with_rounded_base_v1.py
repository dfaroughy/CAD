# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.polygon(points=[(0, 0), (15.77, 31.54), (-15.77, 31.54)])
step3 = step2.extrude(20.00)
step4 = cq.Workplane("XY")
step5 = step4.polygon(points=[(0, 0), (15.77, -31.54), (-15.77, -31.54)])
step6 = step5.extrude(20.00)
step7 = step3.union(step6)
result = step7
