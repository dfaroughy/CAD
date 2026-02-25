# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(100, 50, 50)
step2 = cq.Workplane("XY").workplane(offset=5).box(90, 40, 40)
step3 = step1.cut(step2)
result = step3
