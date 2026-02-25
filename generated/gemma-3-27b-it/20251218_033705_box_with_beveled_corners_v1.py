# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 40, 20)
step2 = cq.Workplane("XY").circle(10).extrude(20)
step3 = step1.faces(">Z").workplane().cut(step2)
result = step3
