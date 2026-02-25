# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 8, 60)
step2 = step1.faces(">Z").workplane().rect(52, 60, centered=True)
step3 = step2.cutThruAll()
result = step1
