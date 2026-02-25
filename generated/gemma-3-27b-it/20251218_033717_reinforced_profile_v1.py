# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(100, 60, 40)
step2 = step1.faces(">Z").workplane().hole(10)
step3 = step1.faces("<Z").workplane().box(90, 50, 30, centered=True)
step4 = step3.faces(">Z").workplane().hole(10)
step5 = step1.union(step3)
result = step5
