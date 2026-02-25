# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(100, 8).extrude(2)
step2 = step1.faces(">Z").workplane().pushPoints([(-40, 0), (40, 0)]).circle(1).cutThruAll()
result = step2
