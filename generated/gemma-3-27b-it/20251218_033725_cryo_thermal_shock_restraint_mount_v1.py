# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 40, 15)
step2 = step1.faces(">Z").workplane().hole(5)
step3 = step1.faces(">Z").workplane().center(15).hole(5)
step4 = step1.faces(">Z").workplane().center(45).hole(5)
step5 = step1.faces(">Z").workplane().center(30).hole(5)
step6 = step1.faces(">Z").workplane().center(15).circle(2.5).extrude(15)
step7 = step1.faces(">Z").workplane().center(45).circle(2.5).extrude(15)
step8 = step1.faces(">Z").workplane().center(30).circle(2.5).extrude(15)
step9 = step1.faces(">Z").workplane().center(15).circle(2.5).extrude(15)
result = step1
