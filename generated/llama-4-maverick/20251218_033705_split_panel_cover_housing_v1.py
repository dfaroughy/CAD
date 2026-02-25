# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(125, 80, 10)
step2 = step1.faces(">Z").workplane().rect(115, 70).cutBlind(-8)
step3 = step2.faces(">X").workplane().center(-57.5, 0).rect(5, 5).cutBlind(-5)
step4 = step3.faces(">Z").workplane().center(0, -30).rect(5, 5).cutBlind(-5)

result = step4
