# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(40, 20).extrude(8)
step2 = step1.faces(">Z").workplane().circle(10).cutBlind(-6)
step3 = step2.faces(">Z").workplane().pushPoints([(8, -6)]).circle(2).cutThruAll()
result = step3
