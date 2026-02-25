# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 15, 50)
step2 = cq.Workplane("XY").transformed(offset=cq.Vector(0, 50, 0)).box(15, 50, 15)
step3 = cq.Workplane("XY").transformed(offset=cq.Vector(0, -50, 0)).box(15, 50, 15)
step4 = cq.Workplane("XY").transformed(offset=cq.Vector(50, 0, 0)).box(15, 50, 15)
step5 = cq.Workplane("XY").transformed(offset=cq.Vector(-50, 0, 0)).box(15, 50, 15)
result = step1.union(step2).union(step3).union(step4).union(step5)
