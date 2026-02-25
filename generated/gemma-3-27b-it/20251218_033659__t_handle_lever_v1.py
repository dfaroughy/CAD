# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(90, 40, 30)
step2 = cq.Workplane("XY").workplane(offset=90).box(90, 40, 30)
step3 = step1.union(step2)
step4 = cq.Workplane("XZ").workplane(at=0).circle(20).extrude(30)
step5 = cq.Workplane("XZ").workplane(at=90).circle(20).extrude(30)
step6 = step4.union(step5)
step7 = step3.cut(step6)

result = step7
