# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(31.54, 31.54)
step2 = step1.vertices().circle(10).extrude(20)
step3 = step2.faces(">Z").wires().toPending().loft(combine=True)
step4 = step3.faces(">Z").fillet(10)

result = step4
