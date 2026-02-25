# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.box(50.0, 50.0, 50.0)
step3 = step2.faces(">Z").workplane().circle(25.0)
step4 = step3.cutThruAll()
result = step4
