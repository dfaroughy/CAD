# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").box(50, 50, 5)
step2 = cq.Workplane("XY").workplane(offset=5).rect(40, 40)
step3 = cq.Workplane("XY").workplane(offset=5).rect(40, 40).extrude(27)
step4 = step3.faces(">Z").workplane().box(5,5,50)
step5 = step3.faces(">Z").workplane().transformed(offset=cq.Vector(0,0,45))
step6 = step3.faces(">Z").workplane().box(5,5,50)
step7 = step3.faces(">Z").workplane(offset=45).box(5,5,5)
step8 = step3.faces(">Z").workplane().transformed(offset=cq.Vector(0,0,45)).box(5,5,50)
step9 = cq.Workplane("XY").workplane(offset=5).rect(40, 40).extrude(27).faces(">Z").workplane().transform((0,0,0), (0,0,1), (40,0,0), angle=90).box(5,50,5)
step10 = step3.faces(">Z").workplane().transformed(offset=cq.Vector(0,0,45)).box(5,5,50)
step11 = step3.faces(">Z").workplane().transformed(offset=cq.Vector(0,0,45)).box(5,5,50)
step12 = step3.faces(">Z").workplane().transformed(offset=cq.Vector(0, 0, 45)).box(5, 5, 50)

result = cq.Workplane("XY").workplane(offset=5).rect(40, 40).extrude(27)
