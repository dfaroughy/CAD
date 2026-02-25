# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(100, 60, 50)
step2 = step1.faces(">Z").workplane().rect(80, 40).cutBlind(-40)
step3 = step2.faces(">Y").workplane().center(-30, -25).rect(20, 20).cutBlind(-10)
step4 = step3.faces(">Y").workplane().center(-30, -25).circle(10).cutBlind(-10)
result = step4
