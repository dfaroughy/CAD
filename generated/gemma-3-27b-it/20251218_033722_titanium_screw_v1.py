# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(8.000, 8.000, 43.000)

step2 = cq.Workplane("XY").transformed(offset=cq.Vector(0, 0, -0.5)).circle(7.999).extrude(8.000)

step3 = step1.union(step2)

result = step3
