# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create a square base
step1 = cq.Workplane("XY").rect(50, 50).extrude(25)

# Step 2: Create a triangular cutout
triangle = cq.Workplane("XY").polygon(3, 50).extrude(25)

# Step 3: Position the triangular cutout
step2 = step1.cut(triangle.translate((0, 0, 25)))

# Step 4: Create another triangular cutout
triangle2 = cq.Workplane("XY").polygon(3, 50).extrude(25)

# Step 5: Position the second triangular cutout
step3 = step2.cut(triangle2.rotate((0, 0, 0), (0, 0, 1), 180).translate((0, 0, 25)))

# Final result
result = step3
