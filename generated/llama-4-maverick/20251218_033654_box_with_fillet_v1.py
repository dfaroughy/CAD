# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(60, 40).vertices().tag("vertices").end()
step2 = step1.vertices(">X or <X").fillet(10)
step3 = step2.extrude(20)
result = step3
