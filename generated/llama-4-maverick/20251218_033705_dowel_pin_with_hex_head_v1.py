# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").circle(4).polygon(6, 10).extrude(8)
step2 = cq.Workplane("XY").box(10, 10, 8)
step3 = step2.faces(">Z").workplane().circle(5).extrude(-18)
step4 = step1.union(step3)
step5 = step4.faces(">Z").edges().fillet(1)
result = step5
