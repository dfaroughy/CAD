# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(90, 40, 30)
step2 = step1.faces(">Z").workplane().circle(15).cutThruAll()
step3 = step2.faces(">Y").workplane().center(-30, 0).circle(2).cutThruAll()
step4 = step3.faces(">Y").workplane().center(30, 0).circle(2).cutThruAll()
step5 = step4.edges("|Z").fillet(2)
result = step5
