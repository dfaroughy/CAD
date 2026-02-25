# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(60, 40).vertices().fillet(10)
step2 = step1.extrude(15)
result = step2
