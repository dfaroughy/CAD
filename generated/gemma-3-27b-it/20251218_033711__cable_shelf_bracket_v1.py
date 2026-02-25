# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(40, 75, 5)
step2 = cq.Workplane("XY").circle(10).extrude(5)
step3 = cq.Workplane("XY").workplane(offset=20).circle(10).extrude(5)
step4 = step1.union(step2)
step5 = step4.union(step3)
result = step5
