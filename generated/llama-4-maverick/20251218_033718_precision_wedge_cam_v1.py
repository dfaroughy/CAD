# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 30, 15)
step2 = cq.Workplane("XY").box(15, 15, 15).translate((30, 0, 7.5))
step3 = step1.union(step2)
step4 = cq.Workplane("XY").box(60, 15, 15).translate((0, 7.5, 0))
step5 = step3.cut(step4).edges("|Z").fillet(2)
result = step5
