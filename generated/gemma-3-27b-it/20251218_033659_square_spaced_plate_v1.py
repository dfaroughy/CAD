# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(100, 10, 10)
step2 = step1.faces(">Z").workplane().hole(5)
step3 = step2.faces(">Z").workplane().translate((0, -30, 0)).hole(5)
step4 = step3.faces(">Z").workplane().translate((0, -60, 0)).hole(5)
step5 = step4.faces(">Z").workplane().translate((0, -90, 0)).hole(5)
step6 = step5.faces(">Z").workplane().translate((90, -5, 0)).cutThruAll(cq.Workplane("XY").box(10, 10, 10))
result = step6
