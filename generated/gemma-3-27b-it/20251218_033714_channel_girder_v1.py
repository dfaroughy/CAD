# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.box(60, 5, 5)
step3 = step2.faces(">Z").workplane()
step4 = step3.polyline([(-5, 0), (0, 5), (60, 5), (60, 0)])
step5 = step4.close()
step6 = step4.extrude(-5)
result = step6
