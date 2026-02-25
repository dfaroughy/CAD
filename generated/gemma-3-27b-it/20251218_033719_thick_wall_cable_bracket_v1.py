# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 40, 15)
step2 = cq.Workplane("XY").workplane(offset=3).rect(54, 34)
step3 = cq.Workplane("XY").workplane(offset=3).rect(54, 34).extrude(-15)
result = step1.cut(step3)
