# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(28.586, 10, 8)
step2 = cq.Workplane("XY").circle(2).translate((0,0,0))
step3 = step1.cut(cq.Workplane("XY").circle(2).translate((0,0,0)))
result = step3
