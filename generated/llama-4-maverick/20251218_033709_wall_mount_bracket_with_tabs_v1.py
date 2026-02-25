# model used: meta-llama/llama-4-maverick
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 50, 1)
step2 = (step1.faces(">Z").workplane()
         .pushPoints([(-25, -20), (25, -20), (-25, 20), (25, 20)])
         .rect(10, 10).cutThruAll())
step3 = (step1.faces(">Z").workplane()
         .pushPoints([(0, -15), (0, 15)])
         .circle(5).cutThruAll())
step4 = (step1.faces(">Z").workplane()
         .moveTo(0, 20).lineTo(10, 20).lineTo(10, 25)
         .lineTo(-10, 25).lineTo(-10, 20).close().cutThruAll())
step5 = (step1.faces(">Z").workplane()
         .moveTo(0, -20).lineTo(10, -20).lineTo(10, -25)
         .lineTo(-10, -25).lineTo(-10, -20).close().cutThruAll())
result = step5
