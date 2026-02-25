# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(60, 50).extrude(5)
step2 = cq.Workplane("XY").rect(50, 40).extrude(5).translate((5, 5, 5))
step3 = step1.cut(step2)
step4 = cq.Workplane("YZ").rect(50, 5).extrude(50).translate((5, 55, 0)).rotate((0,0,1),(0,0,0),90)
step5 = step3.union(step4)
step6 = cq.Workplane("XZ").rect(60, 5).extrude(45).translate((0, 5, 0))
result = step5.union(step6)
