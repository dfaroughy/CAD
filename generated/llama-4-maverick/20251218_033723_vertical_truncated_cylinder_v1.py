# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").circle(25).extrude(50)
step2 = cq.Workplane("XY").box(50, 50, 50, centered=(True, True, False))
step3 = step1.intersect(step2)
result = step3
