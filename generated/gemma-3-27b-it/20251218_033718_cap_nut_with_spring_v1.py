# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").circle(6).extrude(12)
step2 = cq.Workplane("XY").octagon(12).extrude(12)
step3 = step1.union(step2)
result = step3
