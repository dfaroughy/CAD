# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.box(60, 55, 5)
step3 = step2.faces(">Z").workplane()
step4 = step3.circle(2).extrude(-5)
step5 = step2.faces(">Z").workplane().center(15, 27.5).circle(2).extrude(-5)
step6 = step2.faces(">Z").workplane().center(45, 27.5).circle(2).extrude(-5)
result = step6
