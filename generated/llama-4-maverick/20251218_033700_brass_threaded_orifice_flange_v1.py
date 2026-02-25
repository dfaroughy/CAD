# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").circle(100/2).extrude(22)
step2 = cq.Workplane("XY").circle(50/2).extrude(22)
step3 = step1.cut(step2)
step4 = cq.Workplane("XY").circle(100/2).extrude(22/2)
result = step3.union(step4)
