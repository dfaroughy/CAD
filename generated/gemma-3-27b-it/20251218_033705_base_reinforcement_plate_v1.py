# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(120, 8, 8)
step2 = cq.Workplane("XY").circle(4).extrude(8)
step3 = step1.cut(step2)
step4 = cq.Workplane("XY").workplane(offset=40).circle(4).extrude(8)
step5 = step3.cut(step4)
step6 = cq.Workplane("XY").workplane(offset=-40).circle(4).extrude(8)
step7 = step5.cut(step6)
step8 = cq.Workplane("XY").workplane(offset=-40).workplane(offset=80).circle(4).extrude(8)
step9 = step7.cut(step8)
step10 = cq.Workplane("XY").workplane(offset=40).workplane(offset=80).circle(4).extrude(8)
step11 = step9.cut(step10)

result = step11
