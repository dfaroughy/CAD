# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(60, 9).extrude(5)
step2 = step1.edges("|Z").fillet(1)
result = step2
