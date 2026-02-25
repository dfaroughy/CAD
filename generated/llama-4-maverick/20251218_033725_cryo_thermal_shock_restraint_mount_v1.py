# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 40, 15).edges().fillet(1)
step2 = step1.faces(">Z").workplane().center(0,0).circle(4).cutThruAll()
step3 = step2.faces(">Z").workplane().center(0,0).rect(20, 8).cutThruAll()
step4 = step3.faces(">Z").workplane().center(-15,0).circle(4).cutThruAll()
step5 = step4.faces(">Z").workplane().center(15,0).circle(4).cutThruAll()
result = step5
