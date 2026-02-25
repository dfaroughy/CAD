# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main rectangular base
step1 = cq.Workplane("XY").box(60, 40, 20)

# Step 2: Create the inner rectangular cut
step2 = step1.faces(">Z").workplane().rect(40, 20).cutBlind(-10)

# Step 3: Create the central circular hole
step3 = step2.faces(">Z").workplane().circle(10).cutBlind(-20)

# Assign final geometry to result
result = step3
