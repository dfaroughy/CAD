# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").circle(6.0).extrude(12.0)
step2 = cq.Workplane("XY").circle(12.0).extrude(10.0)
step3 = step1.union(step2)
result = step3
