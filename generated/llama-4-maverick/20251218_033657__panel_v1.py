# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(120, 60, 5)
step2 = step1.faces(">Z").workplane().circle(15).cutThruAll()
step3 = step2.faces(">Z").workplane().pushPoints([(-40, -20), (40, -20)]).circle(5).cutThruAll()
step4 = step3.edges("|Z").fillet(2)

result = step4
