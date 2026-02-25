# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.box(25, 25, 46)
step3 = step2.faces(">Z").workplane()
step4 = step3.circle(12.5)
step5 = step4.extrude(-10)
step6 = step2.faces("<Z").workplane()
step7 = step6.polygon(points=[(12.5,0), (0, 12.5), (-12.5,0), (0, -12.5)])
step8 = step7.extrude(-5)
result = step8
