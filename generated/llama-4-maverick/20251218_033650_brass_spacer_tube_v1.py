# model used: meta-llama/llama-4-maverick
python
import cadquery as cq

# Create the base rectangle
step1 = cq.Workplane("XY").box(12, 10, 1)

# Create the outer cylinder
step2 = cq.Workplane("XY").circle(6).extrude(12)

# Create the inner cylinder
step3 = cq.Workplane("XY").circle(5).extrude(12)

# Cut the inner cylinder from the outer cylinder
step4 = step2.cut(step3)

# Intersect the base rectangle with the outer cylinder cutout
step5 = step1.intersect(step4)

# Create the final result by translating the intersected object to the correct position
result = step5.translate((0, 0, 5.5))
