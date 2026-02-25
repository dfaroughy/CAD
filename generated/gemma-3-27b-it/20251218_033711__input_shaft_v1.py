# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").circle(20).extrude(95)
step2 = cq.Workplane("XY").rect(20, 20).extrude(95)
step3 = step1.union(step2)
result = step3
