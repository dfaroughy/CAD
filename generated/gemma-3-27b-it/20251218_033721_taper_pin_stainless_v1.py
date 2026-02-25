# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 9.980, 9.979)
step2 = cq.Workplane("YZ").transformed(offset=cq.Vector(50, 0, 0)).cylinder(9.979, h=9.980)
result = step1.union(step2)
