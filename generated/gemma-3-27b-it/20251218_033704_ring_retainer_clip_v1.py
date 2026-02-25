# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(30, 30, 3)
step2 = cq.Workplane("XY").circle(15)
step3 = cq.Workplane("XY").circle(11)
step4 = step3.extrude(30)
step5 = step4.faces(">Z").workplane().center(0, 0).rect(8, 8)
step6 = step5.cutThruAll()
step7 = step1.union(step4)
result = step7
