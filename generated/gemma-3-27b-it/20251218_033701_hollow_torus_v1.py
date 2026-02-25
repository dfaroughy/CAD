# model used: google/gemma-3-27b-it
import cadquery as cq

step1 = cq.Workplane("XY").circle(25).extrude(5)
step2 = cq.Workplane("XY").circle(12.5).extrude(10)
step3 = cq.Workplane("XY").rect(5, 20).extrude(5)
step4 = cq.Workplane("XY").circle(25).extrude(5)
step5 = cq.Workplane("XY").rect(5, 20).extrude(5)

result = cq.Assembly(name="Part").add(step1, name="outer_cylinder") \
    .add(step2, name="washer1") \
    .add(step3, name="rectangle1") \
    .add(step4, name="outer_cylinder2") \
    .add(step5, name="rectangle2")
