# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 50, 5)
step2 = cq.Workplane("XY").circle(5).extrude(5)
step3 = cq.Workplane("XY").circle(12.5).extrude(5)
step4 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(5).extrude(10))
step5 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(12.5).extrude(10))
step6 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(5).extrude(10))
step7 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(12.5).extrude(10))
step8 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(5).extrude(10))
step9 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(12.5).extrude(10))
step10 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(5).extrude(10))
step11 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(12.5).extrude(10))
step12 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(5).extrude(10))
step13 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(12.5).extrude(10))
step14 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(5).extrude(10))
step15 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(12.5).extrude(10))
step16 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(5).extrude(10))
step17 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(12.5).extrude(10))
step18 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(5).extrude(10))
step19 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(12.5).extrude(10))
step20 = step1.cut(cq.Workplane("XY").workplane(offset=2.5).circle(5).extrude(10))
result = step1
