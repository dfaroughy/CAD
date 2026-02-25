# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(28.586, 8, 10)
step2 = step1.faces(">Z").workplane().center(-8, -3).circle(2.5).cutThruAll()
step3 = step2.faces(">Z").workplane().center(8, -3).circle(2.5).cutThruAll()

result = step3
