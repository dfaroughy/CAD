# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 60, 3)
step2 = cq.Workplane("XY").rect(60, 40).vertices().circle(5).extrude(3)
step3 = step1.cut(step2)
result = step3
