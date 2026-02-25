# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(40, 64, 15)
step2 = step1.faces(">Z").workplane().rect(10, 10).cutBlind(-5)
step3 = step1.faces(">Z").workplane().pushPoints([(-12, -16), (12, -16), (-12, 16), (12, 16)]).circle(3).cutThruAll()
step4 = step1.faces(">Z").workplane().circle(8).cutThruAll()
result = step4
