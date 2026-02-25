# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(60, 50, centered=False).vertices().fillet(5)
step2 = step1.extrude(20)
step3 = cq.Workplane("XY").workplane(offset=20).rect(20, 20, centered=False).extrude(30)
step4 = step2.union(step3.translate((20, 20, 0)))
result = step4
