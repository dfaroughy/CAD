# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(100, 50, 5)
step2 = cq.Workplane("XY").workplane(offset=5).box(100, 40, 5)
step3 = step1.cut(step2)
step4 = cq.Workplane("YZ").workplane(offset=-25).box(5, 50, 100)
step5 = cq.Workplane("YZ").workplane(offset=45).box(5, 40, 100)
step6 = step4.cut(step5)
step7 = step3.union(step6)
result = step7
