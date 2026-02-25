# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(100, 100, 20)
step2 = cq.Workplane("XY").box(60, 60, 20).translate((0, 0, 20))
step3 = step1.union(step2)
step4 = cq.Workplane("XY").pushPoints([(25, 25), (25, -25), (-25, -25), (-25, 25)]).circle(10).extrude(20)
step5 = step3.union(step4)
step6 = cq.Workplane("XY").circle(40).extrude(100).translate((0, 0, 20))
step7 = step5.union(step6)
step8 = cq.Workplane("XY").pushPoints([(25, 25), (25, -25), (-25, -25), (-25, 25)]).circle(5).cutThruAll()
result = step8
