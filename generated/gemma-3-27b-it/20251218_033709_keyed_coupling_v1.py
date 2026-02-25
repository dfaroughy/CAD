# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 50, 8)
step2 = cq.Workplane("XY").circle(45).extrude(8)
step3 = cq.Workplane("XY").workplane(at=0).transformed(offset=cq.Vector(0,0,8)).box(50, 50, 8)
step4 = cq.Workplane("XY").workplane(at=0).transformed(offset=cq.Vector(0,0,16)).box(50, 50, 8)
step5 = step1.union(step2)
step6 = step5.union(step3)
step7 = step6.union(step4)

result = step7
