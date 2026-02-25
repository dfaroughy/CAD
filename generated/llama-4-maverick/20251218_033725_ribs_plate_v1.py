# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(120, 76.5, 18.5)
step2 = step1.faces(">Z").workplane().rect(40, 40).vertices().cboreHole(4.5, 8, 4)
step3 = step2.faces(">Z").workplane().pushPoints([(0, 30)]).rect(10, 5).cutBlind(-4)
step4 = step3.faces(">Y").workplane().center(-30, -8.5+18.5/2).rect(18.5, 18.5).extrude(18.5)
result = step4
