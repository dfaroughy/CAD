# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main cylindrical body
step1 = cq.Workplane("XY").circle(50).extrude(86.603)

# Step 2: Create the flat cut on the top
step2 = step1.faces(">Z").workplane().rect(100, 86.603).cutBlind(-86.603)

# Step 3: Create the slot on the bottom
step3 = step2.faces("<Z").workplane().center(0, -43.3015).rect(20, 10).cutBlind(10)

# Assign final result
result = step3
