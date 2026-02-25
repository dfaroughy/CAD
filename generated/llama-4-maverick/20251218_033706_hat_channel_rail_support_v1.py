# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 40, 7)
step2 = step1.faces(">Z").workplane().rect(60, 20).rect(56, 16).loft(combine=True)
step3 = step2.faces(">Z").workplane().pushPoints([(20, 10), (0, 10), (-20, 10), (20, -10), (0, -10), (-20, -10)]).circle(3).cutThruAll()
step4 = step3.faces(">Z").workplane().pushPoints([(0, 0)]).circle(7.5/2).cutBlind(-40)

result = step4
