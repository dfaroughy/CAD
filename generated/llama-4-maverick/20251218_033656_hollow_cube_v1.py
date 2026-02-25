# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 50, 10)
step2 = cq.Workplane("XY").box(40, 40, 8).translate((0, 0, 1))
step3 = step1.cut(step2)
result = step3
