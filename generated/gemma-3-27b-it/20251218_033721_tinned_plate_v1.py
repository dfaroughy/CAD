# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(80, 60, 3)
step2 = step1.faces(">Z").workplane()
step3 = step2.hole(10).center(20, 20)
step4 = step2.hole(10).center(60, 20)
step5 = step2.hole(10).center(20, 40)
step6 = step2.hole(10).center(60, 40)
result = step6
