# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(80, 70).extrude(25)
step2 = step1.faces(">Z").workplane().rect(40, 20).extrude(10)
step3 = step2.faces(">Z").workplane().center(0, 5).rect(20, 10).extrude(-5)
step4 = step3.faces(">Z").workplane().center(0, 5).slot2D(10, 4, 90).cutBlind(-2)
step5 = step4.faces(">Z").workplane().pushPoints([(-20, -20), (20, -20)]).circle(5).cutThruAll()
step6 = step5.faces(">Y").workplane().center(-30, -12.5).lineTo(10, 0).lineTo(0, -10).close().extrude(25)

result = step6
