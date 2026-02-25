# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(200, 60, 10)
step2 = cq.Workplane("XY").box(180, 40, 10).translate((0, 0, 5))
step3 = step1.cut(step2)
result = step3
