# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.box(10, 50, 7.5)
step3 = step2.faces(">Z").workplane()
step4 = step3.box(10, 50, 7.5)
result = step4
