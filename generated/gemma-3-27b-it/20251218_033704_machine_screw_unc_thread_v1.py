# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY")
step2 = step1.circle(8.0/2.0).extrude(32.0)
step3 = step2.faces(">Z").workplane().circle(6.0/2.0).cutThruAll()
step4 = step2.faces(">Z").workplane().circle(8.0/2.0).extrude(8.0)
step5 = step4.faces(">Z").workplane().circle(6.0/2.0).cutThruAll()
step6 = step2.union(step5)
result = step6
