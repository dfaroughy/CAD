# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base L-shaped profile
step1 = cq.Workplane("XY").rect(50, 30).extrude(50)

# Step 2: Cut the inner L-shape to create the channel
step2 = step1.faces(">Z").workplane().rect(40, 20).cutBlind(-40)

# Step 3: Create the small lip on the open side
step3 = step2.faces(">Y").workplane().rect(10, 10).extrude(10)

# Assign final result
result = step3
