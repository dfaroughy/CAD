# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base box
step1 = cq.Workplane("XY").box(80, 40, 7.5)

# Step 2: Create the inner recessed area
step2 = step1.faces(">Z").workplane().rect(70, 30).cutBlind(-2)

# Step 3: Create the three holes
step3 = step2.faces(">Z").workplane().rarray(25, 0, 3, 1).circle(5).cutBlind(-7.5)

# Assign final result
result = step3
