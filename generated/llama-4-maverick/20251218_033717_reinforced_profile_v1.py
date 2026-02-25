# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(100, 60, 40)
step2 = step1.faces(">Z").workplane().center(0, -20).hole(20)
step3 = step2.faces(">X").workplane().center(0, -20).rect(20, 10).cutBlind(-10)
step4 = step3.edges("|Z").fillet(5)

result = step4
