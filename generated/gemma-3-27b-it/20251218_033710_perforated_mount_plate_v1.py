# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(120, 80, 5)
step2 = cq.Workplane("XY").circle(5).translate((20, 20, 0))
step3 = cq.Workplane("XY").circle(5).translate((20, 60, 0))
step4 = cq.Workplane("XY").circle(5).translate((60, 20, 0))
step5 = cq.Workplane("XY").circle(5).translate((60, 60, 0))
step6 = step1.cut(cq.Workplane("XY").eachpoint([step2, step3, step4, step5], lambda loc: loc.cutThruAll().val()))
result = step6
