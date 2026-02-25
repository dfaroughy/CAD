# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 50, 27, centered=(True, True, False))
step2 = cq.Workplane("XY").box(10, 10, 27, centered=(True, True, False)).translate((0, 0, 27))
step3 = step1.cut(step2)
step4 = cq.Workplane("XY").box(10, 10, 27, centered=(True, True, False)).translate((0, 0, 0))
step5 = step3.union(step4)
result = step5
