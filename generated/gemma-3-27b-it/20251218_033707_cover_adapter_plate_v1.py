# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 60, 8)
step2 = cq.Workplane("XY").circle(40).extrude(8)
step3 = cq.Workplane("XY").center(10, 10).circle(4).extrude(8)
step4 = cq.Workplane("XY").center(10, -10).circle(4).extrude(8)
step5 = cq.Workplane("XY").center(-10, 10).circle(4).extrude(8)
step6 = cq.Workplane("XY").center(-10, -10).circle(4).extrude(8)
step7 = step1.cut(step2)
step8 = step7.cut(step3)
step9 = step8.cut(step4)
step10 = step9.cut(step5)
step11 = step10.cut(step6)
result = step11
