# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Create the base shape
step1 = cq.Workplane("XY").rect(60, 40).vertices().rect(10, 10).extrude(20)

# Create the hole
step2 = cq.Workplane("XY").circle(8).circle(5).extrude(20)

# Cut the hole from the base shape
step3 = step1.cut(step2)

# Add fillets to the edges
step4 = step3.edges("|Z").fillet(2)

# Assign the final geometry to result
result = step4
