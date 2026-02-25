# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(120, 80, 5)
step2 = step1.faces(">Z").workplane().pushPoints([(30, 20), (-30, 20), (-30, -20), (30, -20), (0, 0)]).circle(10).cutThruAll()
step3 = step2.edges("|Z").fillet(2)

result = step3
