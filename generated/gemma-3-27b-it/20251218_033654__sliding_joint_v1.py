# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.box(60, 30, 15)
step3 = step2.faces(">Z").workplane()
step4 = step3.rect(50, 20)
step5 = step4.cutThruAll()
result = step5
