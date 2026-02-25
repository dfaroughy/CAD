# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base cylinder
step1 = cq.Workplane("XY").circle(50).extrude(10)

# Step 2: Create the top cylinder
step2 = step1.faces(">Z").workplane().circle(25).extrude(22)

# Step 3: Create the hole through the entire part
step3 = step2.faces(">Z").workplane().circle(5).cutThruAll()

# Assign final geometry to result
result = step3
