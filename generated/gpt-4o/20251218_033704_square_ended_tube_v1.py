# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the outer box
step1 = cq.Workplane("XY").box(50, 50, 100)

# Step 2: Create the inner box for hollowing
step2 = step1.faces(">Z").workplane().rect(40, 40).cutBlind(-100)

# Step 3: Create the notch at the bottom
step3 = step2.faces("<Z").workplane().center(0, -20).circle(5).cutBlind(5)

# Assign final result
result = step3
