# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base square
step1 = cq.Workplane("XY").rect(31.54, 31.54)

# Step 2: Extrude the square to create a pyramid shape
step2 = step1.extrude(20).edges("|Z").fillet(5.77)

# Step 3: Create a triangle for the top cut
triangle = cq.Workplane("XY").polyline([(0, 0), (15.77, 31.54), (-15.77, 31.54)]).close()

# Step 4: Extrude the triangle to cut the top
step3 = step2.cut(triangle.extrude(20))

# Assign final geometry to result
result = step3
