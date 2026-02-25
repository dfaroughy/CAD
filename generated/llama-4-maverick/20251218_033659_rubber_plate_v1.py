# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(120, 80, 5, centered=(True, True, False))
step2 = step1.faces(">Z").workplane().pushPoints([(-30, -20), (30, -20)]).circle(5).cutThruAll()
step3 = step2.faces(">Z").workplane().center(-40, 0).slot2D(20, 5, 90).cutThruAll()
result = step3
