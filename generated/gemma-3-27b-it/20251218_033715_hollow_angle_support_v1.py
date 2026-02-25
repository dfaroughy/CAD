# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 30, 5)
step2 = step1.faces(">Z").workplane()
step3 = step2.center(25, 15).transformed(offset=cq.Vector(0, 0, -30)).extrude(30)
step4 = step3.faces(">Z").workplane()
step5 = step4.box(50, 5, 30)
result = step3.union(step5)
