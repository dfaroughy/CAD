# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 60, 5)
step2 = step1.faces(">Z").workplane().center(0, 15).slot2D(10, 20, 90).cutThruAll()
step3 = step2.faces(">Z").workplane().center(0, -15).slot2D(10, 20, 90).cutThruAll()
step4 = step3.faces(">Z").workplane().center(-30, 25).circle(3).cutThruAll()
step5 = step4.edges("|Z").fillet(5)

result = step5
