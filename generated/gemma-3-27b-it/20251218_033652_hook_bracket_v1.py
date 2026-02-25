# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 20, 50)
step2 = cq.Workplane("XY").transformed(offset=cq.Vector(0, -10, 0)).box(20, 20, 50)
step3 = step1.union(step2)
step4 = cq.Workplane("XY").transformed(offset=cq.Vector(0, 10, 0)).box(20, 20, 50)
step5 = step3.union(step4)
result = step5
