# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(40, 20, 51.252)
step2 = cq.Workplane("XY").circle(10).extrude(51.252)
step3 = step1.cut(step2)
step4 = cq.Workplane("XY").workplane(offset=20).box(40, 20, 51.252)
step5 = cq.Workplane("XY").workplane(offset=20).circle(10).extrude(51.252)
step6 = step4.cut(step5)
result = cq.Assembly(cq.Location(cq.Vector(0, 0, 0)), step3) + cq.Assembly(cq.Location(cq.Vector(0, 0, 20)), step6)
