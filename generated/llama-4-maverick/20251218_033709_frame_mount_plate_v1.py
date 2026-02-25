# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(80, 60).vertices().circle(2).extrude(5)
step2 = cq.Workplane("XY").rect(60, 40).extrude(5).translate((0, 0, 5))
step3 = step1.cut(step2)
step4 = step3.edges("|Z").fillet(2)

result = step4
