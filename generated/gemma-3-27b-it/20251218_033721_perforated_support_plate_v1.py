# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 80, 5)

step2 = cq.Workplane("XY").circle(10).translate((20, 0)).cutThruAll()

step3 = cq.Workplane("XY").circle(20).translate((40, 0)).cutThruAll()

result = step1
