# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").circle(4).extrude(8)
step2 = cq.Workplane("XY").circle(3.5).extrude(43)
step3 = step1.union(step2)
step4 = cq.Workplane("XY").circle(4).extrude(-8).translate((0,0,43))
step5 = step3.union(step4)
step6 = cq.Workplane("YZ").center(-4,21.5).circle(1).extrude(8)
step7 = step5.cut(step6)
result = step7
