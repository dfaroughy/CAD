# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 55, 5)
step2 = step1.faces(">Z").workplane().center(0, 20).rect(10, 10).extrude(5)
step3 = step2.faces(">Z").workplane().center(0, 20).circle(5).extrude(-5)
step4 = step3.faces(">Z").workplane().center(-15, -10).circle(5).extrude(-5)
step5 = step4.faces(">Z").workplane().center(15, -10).circle(5).extrude(-5)
result = step5
