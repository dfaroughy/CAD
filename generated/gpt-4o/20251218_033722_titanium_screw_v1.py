# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main cylindrical shaft
step1 = cq.Workplane("XY").circle(4).extrude(43)

# Step 2: Create the head of the bolt
step2 = step1.faces(">Z").workplane().circle(4).extrude(8)

# Step 3: Create the inner circle on the head
step3 = step2.faces(">Z").workplane().circle(3.9995).cutBlind(-8)

# Assign final result
result = step3
