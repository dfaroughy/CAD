# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 15, 15)
step2 = cq.Workplane("XY").box(15, 50, 15).translate((0, 0, 7.5))
step3 = step1.union(step2)
step4 = step3.union(step2.rotate((0, 0, 0), (0, 0, 1), 90))
step5 = step4.union(step2.rotate((0, 0, 0), (0, 0, 1), 180))
step6 = step5.union(step2.rotate((0, 0, 0), (0, 0, 1), 270))
step7 = step6.faces(">Z").workplane().center(0, 25).hole(15, 15)
result = step7
