# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 60, 25)
step2 = cq.Workplane("XY").box(50, 30, 12.5).translate((0, 0, 12.5))
step3 = step1.cut(step2)
step4 = cq.Workplane("XY").box(70, 50, 5).translate((0, 0, 25))
step5 = step3.union(step4)
result = step5
