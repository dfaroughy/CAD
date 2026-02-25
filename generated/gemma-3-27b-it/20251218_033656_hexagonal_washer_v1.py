# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(19.691, 17.321, 3.000)

step2 = cq.Workplane("XY").circle(6.0).extrude(3.000)

step3 = step1.cut(step2)

result = step3
