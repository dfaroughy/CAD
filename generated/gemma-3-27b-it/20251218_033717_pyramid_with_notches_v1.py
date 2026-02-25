# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 25, 1)
step2 = cq.Workplane("YZ").box(25, 50, 1).translate((25,0,0))
step3 = cq.Workplane("XY").box(50, 25, 1).translate((0,50,0))
step4 = cq.Workplane("YZ").box(25, 50, 1).translate((75,0,0))
step5 = cq.Workplane("XY").box(50, 25, 1).translate((50,50,0))
step6 = cq.Workplane("XY").box(50, 25, 1).translate((25,25,0))

result = step1.union(step2).union(step3).union(step4).union(step5).union(step6)
