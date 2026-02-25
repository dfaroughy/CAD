# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.box(29.999, 29.999, 30.000)
step3 = step2.faces(">Z").workplane()
step4 = step3.circle(14.9995).extrude(-30.000)
result = step2.cut(step4)
