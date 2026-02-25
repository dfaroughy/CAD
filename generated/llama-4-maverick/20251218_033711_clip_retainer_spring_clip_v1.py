# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(20, 6).extrude(3)
step2 = step1.faces(">Z").workplane().pushPoints([(-6, 0), (6, 0)]).circle(1.5).cutThruAll()
step3 = step2.edges("|Z").fillet(1)
result = step3
