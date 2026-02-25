# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 50, 50)
step2 = step1.faces(">Z").edges().chamfer(2)
step3 = step2.faces("<Z").edges().chamfer(2)
step4 = step3.faces(">X").edges().chamfer(2)
step5 = step4.faces("<X").edges().chamfer(2)
step6 = step5.faces(">Y").edges().chamfer(2)
step7 = step6.faces("<Y").edges().chamfer(2)

result = step7
