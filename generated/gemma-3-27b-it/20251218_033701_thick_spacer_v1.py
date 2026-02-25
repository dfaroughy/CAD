# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.circle(20).extrude(15)
step3 = step2.faces(">Z").workplane()
step4 = step3.circle(16).cutThruAll()
result = step4
