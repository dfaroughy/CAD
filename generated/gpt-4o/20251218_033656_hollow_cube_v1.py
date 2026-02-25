# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the outer box
step1 = cq.Workplane("XY").box(50, 50, 10)

# Step 2: Create the inner box for hollowing
step2 = cq.Workplane("XY").box(40, 40, 10).translate((0, 0, 5))

# Step 3: Cut the inner box from the outer box
result = step1.cut(step2)
