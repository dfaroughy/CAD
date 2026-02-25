# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(30, 20, 39.124, centered=(True, True, False))
step2 = step1.faces(">Z").workplane().circle(7).cutThruAll()
step3 = step2.faces(">Z").workplane().polygon(6, 15).cutBlind(-19.124)
step4 = step3.faces(">Z").workplane().circle(7.5).cutBlind(-3)
step5 = step4.faces(">X").workplane().circle(3).cutThruAll()
result = step5
