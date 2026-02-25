# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(120, 80, 25, centered=(True, True, False))
step2 = step1.faces(">Z").workplane().pushPoints([(30, 20), (-30, 20), (30, -20), (-30, -20)]).hole(8)
step3 = step2.faces(">Z").workplane().pushPoints([(30, 20), (-30, 20), (30, -20), (-30, -20)]).cboreHole(5, 10, 10)
step4 = step3.faces(">X").workplane().center(0, -40).hole(8, 15)
step5 = step4.faces(">X").workplane().center(0, 40).hole(8, 15)

result = step5
