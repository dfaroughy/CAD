# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").rect(7.5, 10).extrude(50)
step2 = cq.Workplane("XY").pushPoints([(3.75, 5)]).circle(2.5).extrude(50)
result = step1.cut(step2)
