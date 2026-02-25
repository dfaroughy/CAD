# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").circle(30/2).circle(15/2).extrude(6)
step2 = cq.Workplane("XY").moveTo(-20/2, 0).rect(20, 6).extrude(6).edges("|Z").fillet(3)
step3 = step1.union(step2)

step4 = cq.Workplane("XZ").moveTo(0, 6).circle(6/2).extrude(30)
step5 = step3.union(step4)

result = step5
