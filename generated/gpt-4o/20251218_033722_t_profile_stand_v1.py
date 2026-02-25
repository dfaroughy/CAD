# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main vertical block
step1 = cq.Workplane("XY").box(20, 40, 60)

# Step 2: Create the horizontal block
step2 = cq.Workplane("XY").box(20, 60, 20).translate((0, 0, 20))

# Step 3: Combine the two blocks
step3 = step1.union(step2)

# Step 4: Create the holes
step4 = step3.faces(">Z").workplane().hole(10).pushPoints([(-20, 0), (20, 0)]).hole(10)

# Assign final geometry to result
result = step4
