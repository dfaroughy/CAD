# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").circle(50).extrude(49.009)
step2 = step1.faces(">Z").workplane().rect(100, 10, centered=(True, False)).cutBlind(-5)
step3 = step1.faces(">Z").workplane().circle(49.9995).extrude(-49.009)
step4 = step3.faces("<Z").workplane().rect(40, 10).cutBlind(10)
result = step2
