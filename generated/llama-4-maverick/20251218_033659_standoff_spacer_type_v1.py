# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").circle(6).circle(4).extrude(10)
step2 = cq.Workplane("XY").box(12, 12, 10, centered=(True, True, False))
step3 = step1.intersect(step2)
step4 = step3.edges("|Z").fillet(0.5)
result = step4
