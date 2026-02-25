# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(10, 7).extrude(50)
step2 = step1.faces(">Z").workplane().rect(10, 7).extrude(-7)
step3 = step2.faces(">Z").edges().fillet(1.5)

result = step3
