# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(100, 50, 50)
step2 = step1.faces(">Z").workplane().rect(90, 40).cutBlind(-10)
step3 = step2.faces(">Y").workplane().center(-25, 0).circle(5).cutThruAll()
step4 = step3.faces(">Z").edges(">X").fillet(5)
step5 = step4.faces(">Z").edges("<X").fillet(5)

result = step5
