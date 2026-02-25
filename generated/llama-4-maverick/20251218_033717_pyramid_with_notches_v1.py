# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Create the base square
step1 = cq.Workplane("XY").box(50, 50, 1)

# Create a triangular prism to be used for cutting
step2 = cq.Workplane("XY").polyline([(0, 25), (25, -25), (-25, -25)]).close().extrude(50)

# Create four rotated versions of the triangular prism
step3 = step2.rotate((0, 0, 0), (0, 0, 1), 90)
step4 = step2.rotate((0, 0, 0), (0, 0, 1), 180)
step5 = step2.rotate((0, 0, 0), (0, 0, 1), 270)

# Cut the triangular prisms from the base square
step6 = step1.cut(step2.translate((12.5, 12.5, 0))).cut(step3.translate((12.5, -12.5, 0)))
step7 = step6.cut(step4.translate((-12.5, -12.5, 0))).cut(step5.translate((-12.5, 12.5, 0)))

# Assign the final geometry to 'result'
result = step7
