# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 60, 5)
step2 = cq.Workplane("XY").pushPoints([(-20, -10), (20, -10)]).circle(5).cutThruAll()
step3 = cq.Workplane("XY").pushPoints([(0, 0)]).circle(15).cutThruAll()
step4 = cq.Workplane("XY").moveTo(30, 0).rect(10, 10).cutThruAll()
step5 = cq.Workplane("XY").moveTo(-30, 0).rect(10, 10).cutThruAll()
result = step1.add(step2).add(step3).add(step4).add(step5)
