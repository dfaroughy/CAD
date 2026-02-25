# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main cylinder
step1 = cq.Workplane("XY").circle(10).extrude(40)

# Step 2: Create the larger cylinder
step2 = cq.Workplane("XY").circle(20).extrude(20)

# Step 3: Combine the two cylinders
step3 = step1.union(step2.translate((0, 0, 20)))

# Step 4: Create the inner hole
step4 = step3.faces(">Z").workplane().circle(9.9995).cutThruAll()

# Assign final geometry to result
result = step4
