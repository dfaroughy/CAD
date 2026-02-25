# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(40, 75).extrude(5)
step2 = cq.Workplane("XY").moveTo(0, 75/2 - 5).circle(5).extrude(5)
step3 = step1.union(step2)
step4 = cq.Workplane("XY").rect(20, 10).extrude(5).translate((0, -75/2 + 15, 0))
step5 = step3.cut(step4)
result = step5
