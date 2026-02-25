# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 50, 50)
step2 = cq.Workplane("XY").circle(25).extrude(50)
step3 = step1.union(step2)
result = step3
