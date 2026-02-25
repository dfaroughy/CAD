# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the hexagonal prism
step1 = cq.Workplane("XY").polygon(6, 21.751).extrude(70)

# Step 2: Create the cylindrical hole
step2 = step1.faces(">Z").workplane().hole(21.731)

# Assign final geometry to result
result = step2
