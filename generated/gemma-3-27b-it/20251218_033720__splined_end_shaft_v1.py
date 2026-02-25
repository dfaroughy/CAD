# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.circle(21.751 / 2).extrude(21.753)
step3 = step2.faces(">Z").workplane()
step3 = step3.center(0, 0).cylinder(70.0, height=21.753)
result = step3
