# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.box(80.0, 60.0, 5.0)
step3 = step2.faces(">Z").workplane()
step4 = step3.circle(10.0).extrude(-10.0)
step5 = step2.faces(">Z").workplane(center=True)
step6 = step5.circle(10.0).extrude(-10.0)
step7 = step2.faces(">Z").workplane(center=True)
step8 = step7.circle(10.0).extrude(-10.0)
result = step2
