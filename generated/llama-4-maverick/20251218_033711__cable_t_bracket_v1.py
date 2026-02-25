# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(30, 42.5).extrude(5)
step2 = step1.faces(">Z").workplane().rect(12, 20).extrude(37.5)
step3 = step2.faces(">Z").workplane().rect(30, 42.5).extrude(-2.5)
step4 = step3.edges("|Z").fillet(2.5)
step5 = step4.edges(">Z and |Y").chamfer(1)
result = step5
