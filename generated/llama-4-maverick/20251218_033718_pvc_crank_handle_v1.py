# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").circle(15).extrude(150)
step2 = step1.faces(">Z").workplane().circle(14.9995).cutBlind(-30)
step3 = step2.faces(">Z").workplane().rect(5,2).cutBlind(-10)

result = step3
