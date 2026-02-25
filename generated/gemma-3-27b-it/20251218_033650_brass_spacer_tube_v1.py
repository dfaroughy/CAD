# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.circle(12.0/2).extrude(10.0)
step3 = step2.faces(">Z").workplane()
step4 = step3.circle(11.999/2).cutThruAll()
step5 = step2.faces(">Z").workplane(center=True)
step6 = step5.circle(12.0/2).extrude(12.0)
step7 = step6.faces(">Z").workplane()
step8 = step7.circle((12.0-0.001)/2).cutThruAll()

result = step8
