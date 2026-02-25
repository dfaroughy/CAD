# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 20, 55)
step2 = cq.Workplane("XY").transformed(offset=cq.Vector(0, 50, 0)).box(20, 50, 20)
step3 = cq.Workplane("XY").transformed(offset=cq.Vector(50, 50, 0)).box(20, 50, 20)
step4 = step1.union(step2)
result = step4.union(step3)
