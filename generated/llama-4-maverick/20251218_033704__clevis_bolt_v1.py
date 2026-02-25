# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(25, 25, 15)
step2 = step1.faces(">Z").workplane().circle(8).polygon(6, 16).extrude(-5, combine=False)
step3 = step1.cut(step2)
step4 = cq.Workplane("XY").box(25, 25, 46).translate((0, 0, 15 + 23))
step5 = step3.union(step4)
result = step5
